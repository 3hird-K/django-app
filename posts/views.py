from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

def posts(request):
    posts = Post.objects.all()

    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_detail(request, slug):

    # return HttpResponse(slug)

    post = Post.objects.get(slug=slug)

    return render(request, 'posts/posts_detail.html', {'post': post})