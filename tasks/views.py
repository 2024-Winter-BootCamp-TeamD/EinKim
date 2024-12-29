from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Task 목록 조회
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Task 생성
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# 개별 Task 편집 (Edit)
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

# 다중 Task 상태 토글 (Toggle Status)
def toggle_tasks_status(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        tasks = Task.objects.filter(id__in=task_ids)
        for task in tasks:
            task.completed = not task.completed
            task.save()
        return redirect('task-list')

# 다중 Task 삭제 확인 페이지 렌더링
def delete_selected(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        tasks = Task.objects.filter(id__in=task_ids)
        return render(request, 'tasks/delete_tasks.html', {'tasks': tasks})

# 다중 Task 삭제 처리
def confirm_delete(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        Task.objects.filter(id__in=task_ids).delete()
        return redirect('task-list')
