from app import app
from flask import  render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# <name> is an example of how to add parameters, here it is ignored
@app.route('/oafishdistortpurp/<name>')
@app.route('/oafishdistortpurp')
def oafishdistortpurp(name=None):
    return render_template('oafishdistortpurp.html',name=name)

@app.route('/phaserlanding')
def phaserlanding():
    return render_template('phasertemplate.html')