from django.conf.urls import url
from . import views 

urlpatterns = [
  url(r'^$', views.index),  
  url(r'^courses/create$', views.create),
  url(r'^courses/confirm/(?P<courses_id>\d+)$', views.confirm), 
  url(r'^courses/delete/(?P<courses_id>\d+)$', views.delete)
]    