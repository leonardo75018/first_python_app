from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('project/<int:id>', views.project),
    path("task/<int:id>", views.task)
]
