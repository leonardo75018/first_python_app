from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.


def hello(request):
    print(id)
    return HttpResponse("<h2>Hello les devs </h2>")


def project(request, id):
    project = list(Project.objects.values())
    return JsonResponse("Project %s" % project, safe=False)


# def project(request, id):
#     project = list(Project.objects.values())

#     return JsonResponse(project, safe=False)


def task(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)

    return HttpResponse("Task %s" % task.title)
