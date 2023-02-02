from django.urls import path

from .views import *


urlpatterns = [
  path('', home, name='home'),
  path('projects', projects, name='projects'),
  path('project/<int:pk>', project, name='project')
]