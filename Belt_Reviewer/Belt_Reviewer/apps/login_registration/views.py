from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_registration/login_registration.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    print result
    if result[0]:
        user = User.objects.filter(email= request.POST['email'])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                messages.error(request, "Welcome {}".format(user.alias))
                request.session['login'] = True
                return redirect('/success')
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Email does not exist")
        return redirect('/')
    else:
        errors = result[1]
        for error in errors:
            messages.error(request, error)
        return redirect('/')


def register(request):
    result = User.objects.validate_registration(request.POST)
    print result
    if result[0]:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=pw_hash)
        user = User.objects.filter(email= request.POST['email'])
        user = user[0]
        request.session['user_id'] = user.id
        request.session['login'] = True
        messages.error(request, "Welcome {}".format(user.alias))
        return redirect('/success')
    else:
        errors = result[1]
        for error in errors:
            messages.error(request, error)
        return redirect('/')

def success(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        return redirect('/books')


def logout(request):
    request.session.clear()
    return redirect('/')
