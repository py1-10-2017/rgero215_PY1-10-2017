from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
# our index route will handle rendering our form
@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')
@app.route('/', methods = ['POST'])
def counter():
    if request.form['ninja']:
        session['counter'] += 1
    return redirect('/')
@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')
# this route will handle our form submission
app.run(debug=True) # run our server
