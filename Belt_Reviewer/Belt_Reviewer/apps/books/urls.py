from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^books$', views.books),
    url(r'^books/add$', views.add, name='add'),
    url(r'^books/create$', views.create),
    url(r'^books/(?P<book_id>\d+)$', views.show),
    url(r'^books/(?P<book_id>\d+)/create$', views.create_additional),
    url(r'^user/(?P<user_id>\d+)$', views.profile),
    url(r'^books/(?P<review_id>\d+)/delete$', views.delete),
]
