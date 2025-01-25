from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer


# Task 목록 조회
class TaskListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of all tasks",
        responses={200: openapi.Response(
            description="A list of tasks",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_OBJECT)
            )
        )}
    )
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Task 생성
class CreateTaskView(APIView):
    @swagger_auto_schema(
        operation_description="Render the task creation form",
        responses={200: "Task creation form rendered"}
    )
    def get(self, request):
        """Render the task creation form."""
        form = TaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})

    @swagger_auto_schema(
        operation_description="Create a new task",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the task')
            },
            required=['title']
        ),
        responses={302: "Redirect to task list after successful creation"}
    )
    def post(self, request):
        """Handle task creation."""
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        return render(request, 'tasks/create_task.html', {'form': form})

# 개별 Task 편집 (Edit)
class EditTaskView(APIView):
    @swagger_auto_schema(
        operation_description="Render the task edit form",
        responses={200: "Task edit form rendered"}
    )
    def get(self, request, pk):
        """Render the task edit form with existing data."""
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(instance=task)
        return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

    @swagger_auto_schema(
        operation_description="Edit an existing task",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Updated title of the task')
            },
            required=['title']
        ),
        responses={302: "Redirect to task list after successful edit"}
    )
    def post(self, request, pk):
        """Handle task editing."""
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

# 다중 Task 상태 토글 (Toggle Status)
class ToggleTasksStatusView(APIView):
    @swagger_auto_schema(
        operation_description="Toggle the completed status of selected tasks",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'task_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="List of task IDs to toggle status"
                )
            },
            required=['task_ids']
        ),
        responses={302: "Redirect to task list after status toggling"}
    )
    def post(self, request):
        task_ids = request.POST.getlist('task_ids')
        tasks = Task.objects.filter(id__in=task_ids)
        for task in tasks:
            task.completed = not task.completed
            task.save()
        return redirect('task-list')


# 다중 Task 삭제 확인 페이지 렌더링
class DeleteSelectedView(APIView):
    @swagger_auto_schema(
        operation_description="Render a confirmation page for deleting selected tasks",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'task_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="List of task IDs to delete"
                )
            },
            required=['task_ids']
        ),
        responses={200: "Rendered confirmation page with selected tasks"}
    )
    def post(self, request):
        task_ids = request.POST.getlist('task_ids')
        tasks = Task.objects.filter(id__in=task_ids)
        return render(request, 'tasks/delete_tasks.html', {'tasks': tasks})


# 다중 Task 삭제 처리
class ConfirmDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete selected tasks",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'task_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="List of task IDs to delete"
                )
            },
            required=['task_ids']
        ),
        responses={302: "Redirect to task list after successful deletion"}
    )
    def post(self, request):
        task_ids = request.POST.getlist('task_ids')
        Task.objects.filter(id__in=task_ids).delete()
        return redirect('task-list')
