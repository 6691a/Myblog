from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AddPostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# def postView(request):
#     post = Post.objects.all()
#     return render(request, "posts.html", {'post': post})


# def postDetailView(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "postDetail.html", {'post': post})


@login_required
def addPostView(request):
    if(request.method == 'POST'):
        # user = User.objects.get(username=request.user.username)
        user = User.objects.get(pk=request.user.pk)
        category = Category.objects.get(pk=request.POST['category'])
        slug = title_to_slug(request)
        # request.POST['title'].lower().replace(' ', '-')

        post = Post()
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


# def post_in_category(request, category_slug=None):
#     # filter를 2번 사용해 퀘리에서 2번 값을 가져오지 않는다
#     # 지연평가 방식 사용 데이터를 사용, 출력하기 전에는 실행되지 않음
#     current_category = None
#     catagories = Category.objects.all()
#     posts = Post.objects.filter(display=True)
#     if category_slug:
#         current_category = get_object_or_404(Category, slug=category_slug)
#         posts = Post.objects.filter(category=current_category)
#     return render(request, 'list.html', {
#         'current_category': current_category,
#         'catagories': catagories,
#         'posts': posts,
#     })


def post_page_category(request, category_slug=None):
    # filter를 2번 사용해 퀘리에서 2번 값을 가져오지 않는다
    # # 지연평가 방식 사용 데이터를 사용, 출력하기 전에는 실행되지 않음
    catagories = Category.objects.all()

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        posts = post_paging(request, 1, current_category)
        # posts = Post.objects.filter(category=current_category)
    else:
        current_category = None
        posts = post_paging(request, 1, category_slug)
        # posts = Post.objects.filter(display=True)

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


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author == request.user:

        # post.delete()
        return redirect('post:post_all')
    else:
        messages.warning(request, "권한이 없습니다.")
        return post_detail(request, id, post.slug)


def post_update(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        if post.author == request.user:
            post.body = request.POST['body']
            post.category = request.POST['category']
            if(post.title != request.POST['title']):
                post.title = request.POST['title']
                post.slug = title_to_slug(request)
            post.save()
            return post_detail(request, id, post.slug)
        else:
            messages.warning(request, "권한이 없습니다.")
            return post_detail(request, id, post.slug)
    else:
        return render(request, 'update.html')


def post_paging(request, page_number, category=None):
    # 웹의 정보 가져오기

    page = request.GET.get('page', '1')

    if category:
        posts = Post.objects.filter(
            category=category, display=True).order_by('-created')
    else:
        posts = Post.objects.filter(display=True).order_by('-created')

    paginator = Paginator(posts, page_number)

    queryset = paginator.get_page(page)
    return queryset


def title_to_slug(request):
    return request.POST['title'].lower().replace(' ', '-')
