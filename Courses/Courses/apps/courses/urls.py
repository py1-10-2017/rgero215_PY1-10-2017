from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^courses$', views.index),
url(r'^courses/(?P<course_id>\d+)/show$', views.show),
url(r'^courses/(?P<course_id>\d+)/destroy$', views.destroy),
]
