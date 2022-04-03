from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    
def about(request):
    return render(request, 'about.html', {'title':'About'})
    