''' lab6 flask proj'''
from flask import Flask
from flask import render_template

# cmd python -m flask --app lab_6 --debug run

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
@app.route('/home')
def index():
    ''' lab6 flask proj'''
    return render_template('home.html')

@app.route('/cookies')
def cookies():
    ''' lab6 flask proj'''
    return render_template('cookies.html')

@app.route('/about')
def about():
    ''' lab6 flask proj'''
    return render_template('about.html')
