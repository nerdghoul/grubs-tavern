from app import app
from flask import  render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/oafishdistortpurp')
def oafishdistortpurp(name=None):
    return render_template('oafishdistortpurp.html',name=name)