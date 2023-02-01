from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request):
  return HttpResponse('Hello from home function')

def project(request: HttpRequest, pk: int):
  return HttpResponse(f'Project wiht pk: {pk}')