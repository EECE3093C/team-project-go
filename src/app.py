from flask import Flask, render_template
app = Flask(__name__)
# set FLASK_DEBUG=1

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")