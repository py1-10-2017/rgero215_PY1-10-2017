from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^surveys$', views.index),     # This line has changed!
url(r'^surveys/new$', views.new)
]
