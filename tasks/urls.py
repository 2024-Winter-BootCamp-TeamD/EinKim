from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.create_task, name='create-task'),
    path('update-tasks/', views.update_tasks, name='update-tasks'),  # 다수 업데이트
    path('delete-tasks/', views.delete_tasks, name='delete-tasks'),  # 다수 삭제
    path('update/<int:pk>/', views.update_task, name='update-task'),  # 개별 업데이트
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),  # 개별 삭제
]