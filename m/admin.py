from django.contrib import admin
import datetime

from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'slug', 'title', 'created')
  list_display_links = ('id', 'slug',)
  prepopulated_fields = {'slug': ('title',)}
  

class ReviewAdmin(admin.ModelAdmin):
  list_display = ('id', 'content', 'created')
  list_display_links = ('id', 'content', ) 


class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

  
admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)