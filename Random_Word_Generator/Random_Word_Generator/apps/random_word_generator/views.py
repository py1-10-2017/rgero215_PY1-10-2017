from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] = 0

    return render(request, 'random_word_generator/index.html')

def generate(request):
    request.session['count'] += 1
    request.session['random_word'] = get_random_string(length = 14)
    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['random_word']
    return redirect('/')
