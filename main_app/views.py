from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

def post_index(request):
    post = Post.objects.all()
    return render(request, 'post/index.html', {'post' : post})

    