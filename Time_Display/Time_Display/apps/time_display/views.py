from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def index(request):
    context = {
        "date": datetime.datetime.now().strftime('%b %d, %Y'),
        "time": datetime.datetime.now().strftime('%I:%M %p')
    }
    return render(request, 'time_display/index.html', context)
