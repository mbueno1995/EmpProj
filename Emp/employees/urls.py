from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('insert', views.insert, name='insert'),
    path('tosave', views.tosave, name='tosave'),
    path('slider', views.slider, name='slider'),
]
