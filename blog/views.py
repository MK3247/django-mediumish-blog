from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from .models import Post

from taggit.models import Tag

from django.db.models import Count

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

def posts (request, tag_slug=None):

    posts = Post.objects.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {

        'posts': posts,
        'tag':tag
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

    post_tags_ids = post.tags.values_list('id', flat=True)
    
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)

    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]

    context = {'post':post, 'similar_posts': similar_posts}

    return render(request, 'post.html', context)

def author(request):

    return render(request, 'author.html', {})