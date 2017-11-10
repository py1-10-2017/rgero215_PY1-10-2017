from django.shortcuts import render, HttpResponse, redirect
from product import items

# Create your views here.
def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']

    context = {
        'items': items
    }
    return render(request, 'amadon/index.html', context)

def process_checkout(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['charged']
    except KeyError:
        request.session['charged'] = 0
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0

    request.session['charged'] += charged
    request.session['total'] += int(request.POST['quantity'])
    request.session['last_transaction'] = charged

    return redirect('/amadon/checkout')

def checkout(request):

    return render(request, 'amadon/checkout.html')

def back(request):
    return redirect('/')
