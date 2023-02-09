from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(blank=True)
  slug = models.SlugField(unique=True)
  review_number = models.IntegerField(default=0)
  review_total = models.IntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  tags = models.ManyToManyField('Tag', related_name="projects")
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('project', kwargs={'slug': self.slug})


class Review(models.Model):
  VOTE = (
    ('up', 'up vote'),
    ('down', 'down vote'),
  )
  
  content = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  vote = models.CharField(max_length=4, choices=VOTE, default=VOTE[0][0])
  project = models.ForeignKey('Project', related_name="reviews", on_delete=models.CASCADE)
  
  
class Tag(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name