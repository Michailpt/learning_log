"""Определени схемы URL для поьзователей"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]