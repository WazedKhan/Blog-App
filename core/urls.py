from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog-home"),
    path('create', views.PostCreateView.as_view(), name="blog-create"),
    path('<int:pk>', views.PostDetailView.as_view(), name="blog-detail"),
    path('about/', views.about, name="blog-about"),
]