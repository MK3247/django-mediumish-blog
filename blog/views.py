from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from .models import Post

def search(request):

    queryset = Post.objects.all()

    query = request.GET.get('q')

    if query:

        queryset = queryset.filter(
            Q(title__icontains = query) |
            Q(body__icontains = query)
        ).distinct()

    context = {
        'queryset':queryset
    }

    return render(request, 'search_result.html', context)


def index(request):

    featured = Post.objects.filter(featured=True)

    posts = Post.objects.order_by('-publish')[0:6]

    context = {

        'featured': featured,

        'posts': posts
    }

    return render(request, 'index.html', context)

def posts (request):

    posts = Post.objects.all()

    context = {

        'posts': posts
    }

    return render(request, 'posts.html', context)

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