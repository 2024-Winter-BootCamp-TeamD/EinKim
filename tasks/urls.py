from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.create_task, name='create-task'),
    path('update/<int:pk>/', views.edit_task, name='edit-task'),
    path('toggle-tasks-status/', views.toggle_tasks_status, name='toggle-tasks-status'),
    path('delete-selected/', views.delete_selected, name='delete-selected'),
    path('confirm-delete/', views.confirm_delete, name='confirm-delete'),
]
