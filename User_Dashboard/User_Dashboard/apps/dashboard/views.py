from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import User
import bcrypt

# Create your views here.
def admin(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        if request.method == 'POST':
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            return redirect('/dashboard/admin')
        else:
            context = {
                'all_users': User.objects.all()
            }
        return render(request, 'dashboard/index.html', context)

def new(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        return render(request, 'dashboard/new.html')

def update(request, user_id):
    # if request.method == 'POST':
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        print '**********{}'.format(request.POST['user_level'])
        if request.POST['user_level'] == 'Admin':
            user.user_level = 9
            user.save()
            return redirect('/dashboard/admin')
        else:
            user.user_level = 1
            user.save()
            return redirect('/dashboard')

    # else:
    #     context = {
    #         'user': User.objects.get(id=user_id)
    #     }
    #     return render(request, 'users_messages/show.html', context)

# def show(request, user_id):
#     context = {
#         'user': User.objects.get(id=user_id)
#     }
#     return render(request, 'users_messages/show.html', context)

def update_password(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        if request.method == 'POST':
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.get(id=user_id)
            user.password = pw_hash
            user.save()
            print '********* Working'
            return redirect('/success')
        else:
            return redirect('/edit')

def edit(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        selected_user = User.objects.get(id=user_id)
        if user.user_level == 9 and user.first_name != selected_user.first_name:
            context = {
                'user': User.objects.get(id=user_id)
            }
            return render(request, 'dashboard/edit.html', context)
        else:
            context = {
                'user': User.objects.get(id=user_id)
            }
            return render(request, 'dashboard/profile.html', context)

def delete(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        User.objects.get(id=user_id).delete()
        return redirect('/')

def description(request):
    user = User.objects.get(id=request.session['user_id'])
    user.description = request.POST['description']
    user.save()
    return redirect('/success')
