from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def projects(request):
    return render(request, 'website/projects.html')