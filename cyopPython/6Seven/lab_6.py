from flask import Flask
from flask import render_template

# cmd python -m flask --app lab_6 --debug run

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
@app.route('/redKeyHomepage')
def index():
    return render_template('redKey1.html')

@app.route('/redKeySignup/')
def red_key2():
    return render_template('redKey2.html')

@app.route('/redKeyTerms/')
def red_key3():
    return render_template('redKey3.html')

