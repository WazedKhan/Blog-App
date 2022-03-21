from django.shortcuts import render


posts = [
    {
        'author':'WazedK',
        'title':'Blog Post-1',
        'content':'Blog Post Content',
        'date':'August 20, 2022'
    },
    {
        'author':'WazedK',
        'title':'Blog Post-2',
        'content':'Blog Post Content',
        'date':'August 21, 2022'
    },
    {
        'author':'WazedK',
        'title':'Blog Post-3',
        'content':'Blog Post Content',
        'date':'August 23, 2022'
    },
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'home.html', context)
    
    
def about(request):
    return render(request, 'about.html', {'title':'About'})
    