from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#rror Create your models here.

class Comment(models.Model):
    content = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('post_index', kwargs={'post_id': self.id}) 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})


