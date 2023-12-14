from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    name='Marinos'
    lastname='Kouvaras'
    return render_template('index.html', myname=name, mylastname=lastname)

@app.route('/name')
def name():
    return "Marinos Kouvaras"

@app.route('/form', methods=['GET', 'POST'])
def show_form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        surname = request.form['surname']
        return render_template('index.html', yourname= name, yoursurname=surname)