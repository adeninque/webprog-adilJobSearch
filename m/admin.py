from django.contrib import admin
import datetime

from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'slug', 'title', 'created')
  list_display_links = ('id', 'slug',)
  prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Project, ProjectAdmin)