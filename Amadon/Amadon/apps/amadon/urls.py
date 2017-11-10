from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^amadon/buy/(?P<item_id>\d+)', views.process_checkout),
url(r'^amadon/checkout$', views.checkout),
url(r'^amadon/back$', views.back)
]
