# ToDo List Application

A simple Django-based ToDo List application with CRUD functionality.

---

## Features

1. **Create**: Add new tasks to your ToDo list.
2. **Read**: View all tasks and their statuses.
3. **Update**: 
   - Edit task details.
   - Toggle completion status of one or multiple tasks.
4. **Delete**:
   - Delete selected tasks with a confirmation step.

---

## Application Structure

### **views.py**

| Function               | Purpose                          | URL Path                |
|------------------------|----------------------------------|-------------------------|
| `task_list`            | View all tasks                  | `/`                     |
| `create_task`          | Create a new task               | `/create/`              |
| `edit_task`            | Edit a specific task            | `/update/<id>/`         |
| `toggle_tasks_status`  | Toggle completion status         | `/toggle-tasks-status/` |
| `delete_selected`      | Display confirmation for delete | `/delete-selected/`     |
| `confirm_delete`       | Confirm and delete tasks        | `/confirm-delete/`      |

---

### **CRUD Features**

1. **Create**
   - Add a new task using the "Create New Task" button on the main page.
   - URL: `/create/`.

2. **Read**
   - View the list of tasks on the main page.
   - URL: `/`.

3. **Update**
   - Edit a task using the "Edit" button next to each task.
   - Toggle multiple tasks' statuses using the "Toggle Status" button.
   - URLs: 
     - `/update/<id>/`
     - `/toggle-tasks-status/`.

4. **Delete**
   - Delete multiple tasks after confirmation.
   - URLs:
     - `/delete-selected/`
     - `/confirm-delete/`.

---

### **Pages and Links**

```plaintext
Main Page (/)
├── Create Page (/create/)
├── Edit Page (/update/<id>/)
├── Toggle Status (/toggle-tasks-status/)
└── Delete Confirmation (/delete-selected/)
    └── Confirm Delete (/confirm-delete/)
```
---

### **Visual Overview**
#### Page Flow Diagram
```plaintext
Main Page (/)
 ├── Create New Task ➡ /create/
 ├── Edit Task ➡ /update/<id>/
 ├── Toggle Task Status ➡ /toggle-tasks-status/
 └── Delete Selected ➡ /delete-selected/ ➡ Confirm Delete ➡ /confirm-delete/
```