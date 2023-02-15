from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .form import CreateNewTask


# Create your views here.


def hello(request):
    title = "Hello les devs 1"
    return render(request, "index.html", {
        "title": title
    })
    # return HttpResponse("<h2>Hello les devs </h2>")


def project(request, id):
    project = list(Project.objects.values())
    return JsonResponse("Project %s" % project, safe=False)


def project(request):
    projects = Project.objects.all()

    return render(request, "projects.html", {
        "projects": projects
    })

    # project = list(Project.objects.values())

    # return JsonResponse(project, safe=False)


def task(request):
    task = Task.objects.all()

    return render(request, "tasks.html", {
        "tasks": task
    })


def create_task(request):
    if request.method == "GET":
        # Show interface
        return render(request, "create_task.html", {
            "form": CreateNewTask()
        })

        # Save data in bdd
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=1
        )
        return redirect("tasks")
