from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def postView(request):
    post = Post.objects.all()
    return render(request, "posts.html", {'post': post})


def postDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "postDetail.html", {'post': post})


def addPostView(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['title']
        post.title_tag = request.POST['title_tag']
        post.save()
        return render(request, "postSuccess.html")
    else:
        return render(request, 'addPost.html')
