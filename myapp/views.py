from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


from .models import Project, Blog, AboutMe

def index(request):
    return render(request, 'index.html')


def portfolio(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio.html', {'projects': projects})


def blog(request):
    blogs = Blog.objects.all()  # Fetch all blog posts
    return render(request, 'blog.html', {'blogs': blogs})


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    about = AboutMe.objects.first()
    return render(request, 'about.html', {'about': about})
