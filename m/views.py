from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .utils import menu, my_projects

# Create your views here.
def home(request):
  return render(request, 'm/home.html', {"title": 'Home'})

def projects(request: HttpRequest):
  return render(request, 'm/projects.html', {'title': 'My projects', 'projects': my_projects, 'menu': menu})

def project(request: HttpRequest, pk: int):
  project = None
  for p in my_projects:
    if p['id'] == pk:
      project = p
  return render(request, 'm/single-project.html', {"title": f"Project {pk}", "pk": pk, "menu": menu, 'project': project})