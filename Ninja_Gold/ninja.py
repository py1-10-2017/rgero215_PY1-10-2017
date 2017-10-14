import random
import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['places'] = []
    return render_template("index.html", session=session['gold'], places=session['places'])

@app.route('/process_money', methods=['POST'])
def game():
    time = datetime.datetime.now()
    if request.form['place'] == 'farm':
        gold = random.randint(10, 20)
        obj = {}
        obj['place'] = 'farm'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        session['gold'] += gold
        session['places'].append(obj)
        return redirect('/')
    elif request.form['place'] == 'cave':
        gold = random.randint(5, 10)
        obj = {}
        obj['place'] = 'cave'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        session['gold'] += gold
        session['places'].append(obj)
        return redirect('/')
    elif request.form['place'] == 'house':
        gold = random.randint(2, 5)
        obj = {}
        obj['place'] = 'house'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        session['gold'] += gold
        session['places'].append(obj)
        return redirect('/')
    elif request.form['place'] == 'casino':
        chances = random.randint(1,2)
        gold = random.randrange(0, 50)
        if chances == 1:
            obj = {}
            obj['place'] = 'casino'
            obj['gold'] = gold
            obj['time'] = time
            obj['won'] = False
            session['gold'] -= gold
            session['places'].append(obj)
            return redirect('/')
        else:
            obj = {}
            obj['place'] = 'casino'
            obj['gold'] = gold
            obj['time'] = time
            obj['won'] = True
            session['gold'] += gold
            session['places'].append(obj)
            return redirect('/')

@app.route('/reset', methods=['POST'])

def reset():
    session.pop('gold', 'places')
    return redirect('/')

app.run(debug=True)
