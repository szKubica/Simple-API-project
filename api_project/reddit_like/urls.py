from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/vote', views.VoteCreate.as_view(), name='add_vote')

]
