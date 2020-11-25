from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# email 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text


def signup(request):
    if request.method == 'POST':

        if request.POST['password'] == request.POST['confirmpassword']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                is_active=False,
                
            )
            message = sendEmail(request, user)
            return render(request, 'authentic.html', {'user': user.email})
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        print( request.POST['username'])
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('posts')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('posts')


def sendEmail(request, user):
    current_site = get_current_site(request)
    message = render_to_string(
        'activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
            'token': account_activation_token.make_token(user),
        })
    mail_title = "My Blog 회원가입 확인 메일"
    mail_to = request.POST['email']
    email = EmailMessage(mail_title, message, to=[mail_to])
    email.send()
    return message


def activate(request, uid64, token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        # 활성화 이후 완료 페이지 보내주기
        # 일단은 메인을 보냄
        return redirect('posts')
    else:  # 비정상 접근 처리
        pass
