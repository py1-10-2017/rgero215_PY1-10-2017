from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# Create your views here.
def index(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/')
    else:
        context = {
            'all_courses': Course.objects.all()
        }
        return render(request, 'courses/index.html', context)

def show(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'courses/show.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
