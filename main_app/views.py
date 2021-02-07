from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def post_index(request):
    post = Post.objects.all()
    return render(request, 'post/index.html', {'post' : post})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/detail.html', {'post' : post})

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'author']

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']

class PostDelete(DeleteView):
    model = Post
    success_url = '/post/'


