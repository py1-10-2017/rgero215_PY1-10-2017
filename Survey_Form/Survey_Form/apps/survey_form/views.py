from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['count'] += 1
    return redirect('/result')

def result(request):
    return render(request, 'survey_form/result.html')

def back(request):
    del request.session['name']
    del request.session['location']
    del request.session['language']
    del request.session['comment']
    return redirect('/')
