from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^users$', views.index),
url(r'^users/new$', views.new),
url(r'^users/(?P<user_id>\d+)$', views.update),
url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
url(r'^users/(?P<user_id>\d+)/delete$', views.delete),
]
