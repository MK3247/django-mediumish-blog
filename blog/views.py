from django.shortcuts import render

from .models import Post

def index(request):

    featured = Post.objects.filter(featured=True)

    posts = Post.objects.order_by('-publish')[0:6]

    context = {

        'featured': featured,

        'posts': posts
    }

    return render(request, 'index.html', context)

def post(request):

    return render(request, 'post.html', {})

def author(request):

    return render(request, 'author.html', {})