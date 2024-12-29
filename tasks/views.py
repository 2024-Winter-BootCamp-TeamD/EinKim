from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Task 목록 조회
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# 개별 Task 생성
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# 개별 Task 업데이트
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.completed = 'completed' in request.POST
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

# 개별 Task 삭제
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/delete_task.html', {'task': task})

# 여러 Task 업데이트
def update_tasks(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')  # 선택된 Task ID 목록 가져오기
        tasks = Task.objects.filter(id__in=task_ids)
        for task in tasks:
            task.completed = not task.completed  # 완료 상태를 반전
            task.save()
        return redirect('task-list')

# 여러 Task 삭제
def delete_tasks(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')  # 선택된 Task ID 목록 가져오기
        Task.objects.filter(id__in=task_ids).delete()
        return redirect('task-list')
