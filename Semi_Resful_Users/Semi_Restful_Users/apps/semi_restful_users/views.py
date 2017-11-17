from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/')
    else:
        context = {
            'all_users': User.objects.all()
        }
    return render(request, 'semi_restful_users/index.html', context)

def new(request):
    return render(request, 'semi_restful_users/new.html')

def update(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=user_id)
        }
        return render(request, 'semi_restful_users/show.html', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful_users/edit.html', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')
