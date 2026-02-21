''' lab6 flask proj'''
from flask import Flask, render_template, request, redirect, url_for,session,flash
from flask import *
import re
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from fileinput import filename
# cmd python -m flask --app test_fiele.py --debug run

app = Flask(__name__)
app.secret_key = "super secret key"

if __name__ == "__main__":
    app.run(debug=True)

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
app_usernames = open('usernames.txt','r',encoding="utf-8")
app_passwords = open('passwords.txt','r',encoding="utf-8")

#sample pass QeX9p0apr+Su
@app.route('/')
@app.route('/registration', methods = ['GET','POST'])
def register():
    '''test_registration'''
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error_message = password_is_valid(password)

        if error_message:
            flash(error_message)

        # elif username in app_usernames:
        #     flash('Username exists')

        # else:
            # username.save(username.usernames)
            # password.save(password.passwords)

            # return redirect(url_for("login_test"))
    return render_template('registration_test.html', username = username, password = password)

@app.route('/login')
def cookies():
    ''' test_login'''
    if request.method == 'GET':
        username = request.form['username']
        password = request.form['password']

    if username in app_usernames:
        session['username'] = username
        flash('Login successful!')
        return redirect(url_for('home'))
    
    return render_template('login_test.html')
