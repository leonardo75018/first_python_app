from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="index"),
    path('projects/', views.project, name="projects"),
    path("tasks/", views.task, name="tasks"),
    path("create_task/", views.create_task, name="create_task")
]
