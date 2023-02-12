from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('todo-details/<id>/', views.todo_details, name='todo-details'),
    path('todo-delete/<id>/', views.todo_delete, name='todo-delete'),
    path('edit-todo/<id>/', views.todo_edit, name='todo-edit'),
]