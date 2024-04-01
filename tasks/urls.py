from django.urls import path 
from .views import index, task_list, task_detail, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView
urlpatterns = [
    path('', index, name='index'),
    path('create', TaskCreateView.as_view(), name='create'),
    path('list', task_list, name='list'),
    path('<int:pk>/detail', TaskUpdateView.as_view(), name='task-detail'),
]

app_name = 'tasks'
