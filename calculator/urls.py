from django.contrib import admin
from django.urls import path,include
from .views import homepage,contactus,blog

urlpatterns = [
    path('home',homepage ,name='homepage'),
    path('contactus/',contactus,name='contactus'),
    path('blog/',blog,name='blog')
]