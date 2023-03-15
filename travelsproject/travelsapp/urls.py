from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
   # path('', views.orgin, name='orgin'),
   # path('', views.original, name='original'),


]
