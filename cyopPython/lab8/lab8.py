''' lab7 flask proj'''
import re
import logging
import difflib
from flask import Flask, render_template, request, redirect, url_for,flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session

# cmd python -m flask --app lab8.py --debug run

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

def file_logger():
    '''Provides logging for routes'''
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # file handler
    fh = logging.FileHandler('test.log')
    fh.setLevel(logging.DEBUG)

    # formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # handler
    logger.addHandler(fh)
    return logger
logger = file_logger()


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
def common_passwords(password):
    '''checks user password against common ones'''
    with open('CommonPasswords.txt','r', encoding="utf-8") as f:
        words = [line.strip() for line in f]
    n = 3
    cutoff = 0.5
    close_passwords = difflib.get_close_matches(password,words,n,cutoff)

    if close_passwords:
        return 'The password you entered was found in a list of common passwords'
    return None
def find_user(username):
    '''looks for username, user inputs'''
    with open('usernames.txt',encoding="utf-8") as f:
        read_data = f.read()
    if username not in read_data:
        return 'Username not found'
    return None
def load_users():
    '''loads users for functions'''

    users = {}

    with open('usernames.txt','r',encoding="utf-8") as f:
        for line in f:
            username,hashed_password = line.strip().split(':', 1)
            users[username] = hashed_password
    return users

# T-tra0R6!RiM
@app.route('/registration', methods = ['GET','POST'])
def register():
    '''test_registration'''

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        error = None
        invalid_password = password_is_valid(password)
        common_password = common_passwords(password)
        invalid_username = user_is_valid(username=username)

        if invalid_password:
            error = invalid_password
            flash(error)
            return render_template('registration.html', error=error)

        if common_password:
            error = common_password
            flash(common_password)
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
    print(session)
    if request.method == "POST":
        logger.warning("failed login attempt:")

        username = request.form["username"]
        password = request.form["password"]
        users = load_users()


        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash("Logging in")
            return redirect(url_for('home'))
        flash("invalid username or password")
    return render_template('login.html')

@app.route('/logout')
def logout():
    '''clears session'''
    session.clear()
    return redirect(url_for('login'))

@app.route('/reset-password', methods =['GET','POST'])
def password_reset():
    '''user can reset password'''

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None
        invalid_password = password_is_valid(password)
        user_not_found = find_user(username)

        if invalid_password:
            error = invalid_password
            flash(error)
            return render_template('password-reset.html', error=error)

        if user_not_found:
            error = user_not_found
            flash(error)
            return render_template('password-reset.html', error=error)

        hashed_password = generate_password_hash(password)
        users[username] = hashed_password

        if username in users and check_password_hash(users[username], password):
            with open('passwords.txt','a',encoding="utf-8") as f:
                f.write(hashed_password + '\n')

            with open('usernames.txt','a',encoding="utf-8") as f:
                f.write(f"{username}:{hashed_password}\n")

        flash('Reset complete')
        return redirect(url_for('login'))
    return render_template('password-reset.html')


@app.route('/home')
def home():
    '''user clicks buttons to navigate website'''
    print(session)
    if not session.get('username'):
        return redirect("login")
    return render_template("home.html")

@app.route('/cookies')
def cookies():
    ''' user is displayed cookies'''
    if not session.get('username'):
        return redirect("login")
    return render_template('cookies.html')

@app.route('/about')
def about():
    ''' user is displayed content about author'''
    if not session.get('username'):
        return redirect("login")
    return render_template('about.html')
