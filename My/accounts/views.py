from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmpassword']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                is_active=False,
            )

            #auth.login(request, user)
            print(user.email)
            return render(request, 'authentic.html', {'user': user.email})
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('posts')
            else:
                # 가입은 했으나 이메일 인증을 안받음 그떄 이동 시킬 곳
                pass
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('posts')
