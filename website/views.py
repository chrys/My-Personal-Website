from django.shortcuts import render
from blog.models import BlogPage

def home(request):
    latest_post = BlogPage.objects.live().public().order_by('-first_published_at').first()
    return render(request, 'website/home.html', {
        'latest_post': latest_post
    })

def projects(request):
    return render(request, 'website/projects.html')