from django.shortcuts import render
from .models import MyProject

def projects_list(request):
    projects = MyProject.objects.all()
    return render(request, 'portfolio/projects_list.html', {
        'projects': projects
    })
