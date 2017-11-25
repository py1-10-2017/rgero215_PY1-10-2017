from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^login_registration$', views.login_registration),
url(r'^login$', views.login),
url(r'^register$', views.register),
url(r'^success$', views.success),
url(r'^logout$', views.logout),
]
