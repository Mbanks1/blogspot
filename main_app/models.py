from django.db import models
from django.contrib.auth.models import User
#rror Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
