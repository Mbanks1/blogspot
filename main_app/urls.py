from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post_index, name='index'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:post_id>/', views.post_detail, name='detail'),
]