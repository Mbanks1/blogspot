from django.shortcuts import render, redirect
from django.views.generic import ListView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def posts_index(request):
    return render(request, 'posts/index.html')