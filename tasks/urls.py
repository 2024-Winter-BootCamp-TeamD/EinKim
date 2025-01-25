from django.urls import path
from .views import TaskListView, CreateTaskView, EditTaskView, ToggleTasksStatusView, DeleteSelectedView, ConfirmDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', CreateTaskView.as_view(), name='create-task'),
    path('edit/<int:pk>/', EditTaskView.as_view(), name='edit-task'),
    path('toggle-status/', ToggleTasksStatusView.as_view(), name='toggle-tasks-status'),
    path('delete-selected/', DeleteSelectedView.as_view(), name='delete-selected'),
    path('confirm-delete/', ConfirmDeleteView.as_view(), name='confirm-delete'),
]
