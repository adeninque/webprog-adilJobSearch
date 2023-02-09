from django.urls import path

from .views import *


urlpatterns = [
  path('', home, name='home'),
  path('projects', projects, name='projects'),
  path('project/<slug:slug>', project, name='project')
]