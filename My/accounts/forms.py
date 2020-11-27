from django import forms
from django.contrib.auth.models import User
from django.contrib import messages

# 사용 안함


class SignupForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': '123',
            'email': None,

        }

    def clean_password1(self, clean_data):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("비밀번호가 다릅니다.")
        return password1

    def clean_username(self):

        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("아이디 중복")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이메일 중복")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.is_active = False
        if commit:
            user.save()
        return user


def clean(request):
    if clean_email(request) and clean_id(request) and clean_password(request):
        return True
    return False


def clean_email(request):
    email = request.POST['email']
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email이 중복 되었습니다.', extra_tags='email')
        print('Email이 중복 되었습니다.')
        return False
    return True


def clean_password(request):
    pw1 = request.POST['password']
    pw2 = request.POST['confirmpassword']

    if pw1 != pw2:
        messages.error(request, '비밀번호가 동일하지 않습니다.', extra_tags='password')
        print('비밀번호가 동일하지 않습니다.')
        return False
    else:
        if int(len(pw2)) < 7:
            messages.error(request, '비밀번호가 7글자 미만입니다.', extra_tags='password')
            print('비밀번호가 7글자 미만입니다.')
            return False
    return True


def clean_id(request):
    id = request.POST['username']

    if int(len(id)) < 5:
        messages.error(request, 'ID 길이가 5글자 미만입니다', extra_tags='id')
        print('ID 길이가 5글자 미만입니다')
        return False
    else:
        if User.objects.filter(username=id).exists():
            messages.error(request, 'ID가 중복 되었습니다.', extra_tags='id')
            print('ID가 중복 되었습니다.')
            return False
    return True


def create_user(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
        is_active=False,
    )
    return user
