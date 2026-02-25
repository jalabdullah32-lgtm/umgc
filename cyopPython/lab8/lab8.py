''' lab7 flask proj'''
import re
from flask import Flask, render_template, request, redirect, url_for,flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from flask import *


# cmd python -m flask --app test_fiele.py --debug run

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
if __name__ == "__main__":
    app.run(debug=True)

users = {}
def password_is_valid(password):
    """
    Validate the password complexity.
    Args:
    password (str): The password to validate.
    Returns:
    str: Error message if password is invalid, None if password is valid.
    """
    if len(password) < 12:
        return 'Password must be at least 12 characters long.'
    if not re.search("[a-z]", password):
        return 'Password must contain at least one lowercase letter.'
    if not re.search("[A-Z]", password):
        return 'Password must contain at least one uppercase letter.'
    if not re.search("[0-9]", password):
        return 'Password must contain at least one number.'
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return 'Password must contain at least one special character.'
    return None
def user_is_valid(username):
    '''Checks to see if username is taken'''
    with open('usernames.txt',encoding="utf-8") as f:
        read_data = f.read()
    if username in read_data:
        return 'Username is already taken, please try again'
    return None

@app.route('/registration', methods = ['GET','POST'])
def register():
    '''test_registration'''

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        error = None
        invalid_password = password_is_valid(password)
        invalid_username = user_is_valid(username=username)

        if invalid_password:
            error = invalid_password
            flash(error)
            return render_template('registration.html', error=error)

        if invalid_username:
            error = invalid_username
            flash(error)
            return render_template('registration.html', error=error)

        hashed_password = generate_password_hash(password)
        users[username] = hashed_password
        with open('usernames.txt','a',encoding="utf-8") as f:
            f.write(f"{username}:{hashed_password}\n")
        with open('passwords.txt','a',encoding="utf-8") as f:
            f.write(hashed_password + '\n')
        with open('email.txt','a',encoding="utf-8") as f:
            f.write(email + '\n')

        flash('Registration complete')
        return redirect(url_for('login'))
    return render_template('registration.html')

@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():
    ''' test_login'''
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            session['logged_in'] = True
            flash("Logging in")
            return redirect(url_for('home'))
        flash("invalid username or password")
    return render_template('login.html')

@app.route('/home')
def home():
    '''user clicks buttons to navigate website'''    
    if not session.get('username'):
        return redirect("/login")
    return render_template('home.html')

@app.route('/cookies')
def cookies():
    ''' user is displayed cookies'''
    if not session.get('username'):
        return redirect("/login")

    return render_template('cookies.html')

@app.route('/about')
def about():
    ''' user is displayed content about author'''
    if not session.get('username'):
        return redirect("/login")
    return render_template('about.html')
