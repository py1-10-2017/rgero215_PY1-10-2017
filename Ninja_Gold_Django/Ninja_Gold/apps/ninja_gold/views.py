from django.shortcuts import render, HttpResponse, redirect
import datetime
import random


# Create your views here.
def index(request):
    try:
        request.session['gold']
        request.session['places']
    except KeyError:
        request.session['gold'] = 0
        request.session['places'] = []

    return render(request, 'ninja_gold/index.html')

def process(request):
    time = datetime.datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    if request.POST['place'] == 'farm':
        gold = random.randint(10, 20)
        obj = {}
        obj['place'] = 'farm'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        request.session['gold'] += gold
        request.session['places'].append(obj)

    elif request.POST['place'] == 'cave':
        gold = random.randint(5, 10)
        obj = {}
        obj['place'] = 'cave'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        request.session['gold'] += gold
        request.session['places'].append(obj)

    elif request.POST['place'] == 'house':
        gold = random.randint(2, 5)
        obj = {}
        obj['place'] = 'house'
        obj['time'] = time
        obj['gold'] = gold
        obj['won'] = True
        request.session['gold'] += gold
        request.session['places'].append(obj)

    elif request.POST['place'] == 'casino':
        chances = random.randint(1,2)
        gold = random.randrange(0, 50)
        if chances == 1:
            obj = {}
            obj['place'] = 'casino'
            obj['gold'] = gold
            obj['time'] = time
            obj['won'] = False
            request.session['gold'] -= gold
            request.session['places'].append(obj)

        else:
            obj = {}
            obj['place'] = 'casino'
            obj['gold'] = gold
            obj['time'] = time
            obj['won'] = True
            request.session['gold'] += gold
            request.session['places'].append(obj)

    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['places']

    return redirect('/')
