"""View management for the blog app."""
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Post


def index(request):
    """Index page listing all the posts."""
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    """Get detailed view of a particular post."""
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def posts_for_user(request, username):
    """Get all the posts for a particular user."""
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'blog/posts_for_user.html', 
        {'user': user, 
        'posts': posts})