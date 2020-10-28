from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages

# Create your views here.


def index(request):
    allposts = Post.objects.all()
    # print(allposts)
    context = {'allposts': allposts}
    return render(request, 'blog/index.html', context)


def blog_post(request, slug):
    posts = Post.objects.filter(slug=slug).first()
    context = {'post': posts, }
    return render(request, 'blog/post.html', context)
