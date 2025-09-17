from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)    
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)    
  

    def __str__(self):
        return self.title