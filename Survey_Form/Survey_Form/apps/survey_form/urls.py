from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^surveys/process$', views.process),
url(r'^result$', views.result),
url(r'^back$', views.back)
]
