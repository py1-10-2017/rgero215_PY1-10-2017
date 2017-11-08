from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),    # This line has changed!
url(r'^process/success$', views.process),
url(r'^process/reset$', views.reset)
]
