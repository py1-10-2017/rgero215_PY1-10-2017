from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^dashboard$', views.admin),
    url(r'^dashboard/admin$', views.admin),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<user_id>\d+)$', views.update),
    url(r'^description$', views.description),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/update_password$', views.update_password),
    url(r'^users/(?P<user_id>\d+)/delete$', views.delete),
]
