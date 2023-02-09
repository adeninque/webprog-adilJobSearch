from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .utils import menu, get_user_context
from .models import Project

# Create your views here.
def home(request):
  context = get_user_context(title = 'Home')
  return render(request, 'm/home.html', context=context)

def projects(request: HttpRequest):
  my_projects = Project.objects.all()
  return render(request, 'm/projects.html', {'title': 'My projects', 'projects': my_projects, 'menu': menu})

def project(request: HttpRequest, slug: str):
  project: Project = Project.objects.get(slug = slug)
  context = get_user_context(
    title = project.title,
    project = project
  )
  return render(request, 'm/single-project.html', context=context)