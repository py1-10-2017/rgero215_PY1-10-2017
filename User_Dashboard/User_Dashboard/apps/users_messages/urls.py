from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^users/show/(?P<user_id>\d+)$', views.show),
    url(r'^users/show/(?P<user_id>\d+)/post$', views.message),
    url(r'^users/show/(?P<user_id>\d+)/comment$', views.comment),
    # url(r'^users/(?P<user_id>\d+)', views.messages)
]
