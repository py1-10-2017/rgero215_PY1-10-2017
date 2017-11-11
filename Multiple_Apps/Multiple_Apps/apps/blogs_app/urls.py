from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^blogs$', views.index),     # This line has changed!
url(r'^blogs/new$', views.new),
url(r'^blogs/create$', views.create),
url(r'^blogs/(?P<number_id>\d+)$', views.show),
url(r'^blogs/(?P<number_id>\d+)/edit$', views.edit),
url(r'^blogs/(?P<number_id>\d+)/delete$', views.destroy)
]
