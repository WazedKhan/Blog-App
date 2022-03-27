from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="posts"),
    path('create', views.create, name="post.create"),
]