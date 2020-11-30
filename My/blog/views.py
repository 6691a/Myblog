from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AddPostForm
from django.contrib.auth.models import User


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
        category = Category.objects.get(pk=request.POST['category'])
        slug = request.POST['title'].lower().replace(' ', '-')

        post = Post()
        print(request.POST)
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.author = user
        post.slug = slug
        post.category = category
        post.save()
        return redirect('post:post_all')
        # return render(request, "postSuccess.html")
    else:
        form = AddPostForm()
        return render(request, 'addPost.html', {'form': form})


def post_in_category(request, category_slug=None):

    # filter를 2번 사용해 퀘리에서 2번 값을 가져오지 않는다
    # 지연평가 방식 사용 데이터를 사용, 출력하기 전에는 실행되지 않음
    current_category = None
    catagories = Category.objects.all()
    print(catagories)
    posts = Post.objects.filter(display=True)
    if category_slug:
        print(category_slug)
        current_category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=current_category)
    return render(request, 'list.html', {
        'current_category': current_category,
        'catagories': catagories,
        'posts': posts,
    })


def post_detail(request, id, post_slug=None):
    posts = get_object_or_404(Post, id=id, slug=post_slug)
    return render(request, 'detail.html', {
        'posts': posts
    })
