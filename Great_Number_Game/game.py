import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['winner'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/', methods=['POST'])
def game():
    return redirect('/')

app.run(debug=True)
