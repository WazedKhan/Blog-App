from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog-home"),
    path('create', views.PostCreateView.as_view(), name="blog-create"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', views.PostDeleteVIew.as_view(), name="blog-delete"),
    path('about/', views.about, name="blog-about"),
]