from re import sub
from flask import Flask, request
import subprocess

from flask.templating import render_template

app = Flask(__name__, template_folder='./')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ping", methods=['POST'] )
def ping():
    address= request.form['address']

    return subprocess.check_output(['sh', '-c', f'ping -c 3 {address}']).decode('UTF8').replace('\n', '<br>' )




    

    