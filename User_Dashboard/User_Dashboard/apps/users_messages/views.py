from django.shortcuts import render, HttpResponse, redirect
from .models import Message, Comment
from ..login_registration.models import User

# Create your views here.
def show(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        this_user = User.objects.get(id=user_id)
        messages = this_user.messages.all().order_by('-created_at')

        context = {
            'user': User.objects.get(id=user_id),
            'messages_obj': messages,
        }



        for message in messages:
            this_message = Message.objects.get(id=message.id)
            comments = this_message.comments.all()

            context['comments'] = comments
        context['messages_obj'] = messages

        return render(request, "users_messages/show.html", context)

def message(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        message = request.POST['message']
        context = {
            'user': User.objects.get(id=user_id),
            'messages_obj': message
        }
        id = request.session['user_id']
        user = User.objects.get(id=id)
        created_by = user.first_name +' '+user.last_name
        this_user = User.objects.get(id=user_id)
        print '*********{}********'.format(this_user)
        message_query = Message.objects.create(created_by=created_by, message=message)
        this_message = Message.objects.get(id=message_query.id)
        this_message.user.add(this_user)
        context['messages_obj'] = message_query
        return redirect('/users/show{}'.format('/'+user_id))
        #return redirect(redirect_to)

def comment(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        comment = request.POST['comment']
        context = {
            'user': User.objects.get(id=user_id),
            'comment': comment
        }
        id = request.session['user_id']
        user = User.objects.get(id=id)
        message_id = request.POST['message_id']
        created_by = user.first_name +' '+user.last_name
        this_message = Message.objects.get(id=message_id)
        print '*********{}********'.format(this_message.id)
        comment_query = Comment.objects.create(created_by=created_by, message_id=this_message.id, comment=comment)
        this_comment = Comment.objects.get(id=comment_query.id)
        print '*********{}********'.format(comment_query.id)
        this_comment.message.add(this_message)
        context['comment'] = comment_query
        # return render(request, 'users_messages/show.html', context)
        return redirect('/users/show{}'.format('/'+user_id))
