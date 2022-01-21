from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):

    featured = Post.objects.filter(featured=True)

    posts = Post.objects.order_by('-publish')[0:6]

    context = {

        'featured': featured,

        'posts': posts
    }

    return render(request, 'index.html', context)

def post_detail(request, year, month, day, post):

    post = get_object_or_404 (
        Post, 
        publish__year = year, 
        publish__month = month,
        publish__day = day,
        slug = post,
        status = 'published'
    )

    related = Post.objects.order_by('-publish')[0:3]

    context = {

        'post':post,

        'related': related

    }

    return render(request, 'post.html', context)

def author(request):

    return render(request, 'author.html', {})