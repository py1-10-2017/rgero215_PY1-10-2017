from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    print result
    if result[0]:
        user = User.objects.filter(email= request.POST['email'])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                messages.error(request, "Welcome {}".format(user.first_name))
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
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        user = User.objects.filter(email= request.POST['email'])
        user = user[0]
        request.session['user_id'] = user.id
        messages.error(request, "Welcome {}".format(user.first_name))
        return redirect('/success')
    else:
        errors = result[1]
        for error in errors:
            messages.error(request, error)
        return redirect('/')

def success(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_registration/show.html', context)
