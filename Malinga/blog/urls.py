from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'blog';

urlpatterns = [
    re_path('home', views.home, name='home'),
    path('category', views.cate, name='category'),
    re_path('blogs', views.blogs, name='blogs'),
    path('post/<int:pk>/', views.blog, name='post'),
    path('post/<int:pk>/',views.BlogView.as_view(), name='post'),
    path('admin2', views.admin, name='admin'),
    
]

