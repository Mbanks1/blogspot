from django.db import models
from django.contrib.auth.models import User
#rror Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title + '|' + self.author
    
