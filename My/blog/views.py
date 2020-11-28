from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm
from django.contrib.auth.models import User
# Create your views here.


def postView(request):
    post = Post.objects.all()
    return render(request, "posts.html", {'post': post})


def postDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "postDetail.html", {'post': post})


def addPostView(request):
    if(request.method == 'POST'):
        # user = User.objects.get(username=request.user.username)

        user = User.objects.get(pk=request.user.pk)
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['title']
        post.author = user
        post.save()
        return redirect('posts')
        # return render(request, "postSuccess.html")
    else:
        form = AddPostForm()
        return render(request, 'addPost.html', {'form': form})
