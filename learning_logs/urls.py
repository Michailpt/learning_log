"""Определяет схемы URL для lerning_logs"""
from django.urls import path  # Импортирует функцию path из модуля django.urls, необходимую для создания URL-схем.
from . import views  # Импортирует модуль views из текущего пакета (текущего каталога), содержащий представления Django.

app_name = 'learning_logs'  # Задает префикс для пространства имен URL, обеспечивая уникальность для данного приложения.
urlpatterns = [
    path('', views.index, name='index'),  # домашняя страница. Определяет URL-шаблон для домашней страницы. При обращении к корневому URL вызывается представление index из модуля views. Присваивает имени 'index'.
    path('topics/', views.topics, name='topics'),  # страница topics
    path('topic/<int:topic_id>/', views.topic, name='topic'),  # страница topic
    path('new_topic/', views.new_topic, name='new_topic'),  # страница new_topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # страница new_entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # страница edit_entry
]
