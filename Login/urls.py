from django.contrib import admin
from django.urls import path, include 
from django.urls import path
from Login import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('Login', views.Login)
]