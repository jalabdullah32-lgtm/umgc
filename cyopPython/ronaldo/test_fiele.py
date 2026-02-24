''' lab6 flask proj'''
from flask import Flask, render_template, request, redirect, url_for,flash, session
from flask import *
import re
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pandas as pd
from fileinput import filename

# cmd python -m flask --app test_fiele.py --debug run

app = Flask(__name__)
app.secret_key = "super secret key"

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

    # user_file = open('usernames.txt','r')
    # if username in user_file:
    #     return 'Username is already taken, please again'

    with open('usernames.txt',encoding="utf-8") as f:
        read_data = f.read()
    if username in read_data:
        return 'Username is already taken, please try again'
def get_usernames(username):
    with open('usernames.txt',encoding="utf-8") as f:
        read_data = f.read()
        if username not in read_data:
            return 'Username not found in database'




@app.route('/')
@app.route('/registration', methods = ['GET','POST'])
def register():
    '''test_registration'''


    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None
        invalid_password = password_is_valid(password)
        invalid_username = user_is_valid(username=username)
        # user =  get_usernames(username=username)

        if invalid_password:
            error = invalid_password
            flash(error)
            return render_template('registration_test.html', error=error)

        if invalid_username:
            error = invalid_username
            flash(error)
            return render_template('registration_test.html', error=error)

        else:
            hashed_password = generate_password_hash(password)
            users[username] = hashed_password
            with open('usernames.txt','a',encoding="utf-8") as f:
                f.write(f"{username}:{hashed_password}\n")
            with open('passwords.txt','a',encoding="utf-8") as f:
                f.write(hashed_password + '\n')

            flash('Registration complete')
            return redirect(url_for('cookies'))
    return render_template('registration_test.html')

@app.route('/login', methods = ['GET','POST'])
def cookies():
    ''' test_login'''
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        # check_username = get_usernames(username=username)
        # error = None


        if username in users and check_password_hash(users[username], password):
                session['username'] = username
                flash('Login true')
                return redirect(url_for('index'))
        else:
            flash('invalid username or password')


        # if check_username:
        #     error = check_username
        #     flash(error)
        #     return render_template('login_test.html')
        
        # else:
        #     session['username'] = username
        #     session['password'] = password
        #     flash('Login true')
        #     return redirect(url_for('index'))

        #     if username in user_file and check_password_hash(pwhash=password):
        #         session[username] = username
        #         flash('logged in')
        #         return redirect(url_for('index'))
        # flash('Invalid Username or Pass')
        # return render_template('login_test.html')

            # invalid_username = user_is_valid(username=username)
            # if invalid_username:
            #     flash(invalid_username)
        #     return render_template('login_test.html', invalid_username=invalid_username)
    return render_template('login_test.html')

@app.route('/home')
def index():
    ''' lab6 flask proj'''
    if 'username' in session:
        return render_template('home.html')
    return render_template('home.html')

