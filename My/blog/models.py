from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="")
    # 작성자를 포린키(유저)로 설정 유저가 사라지면 작성 글 또한 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # admin 노출될 형식

    def __str__(self):
        return "작성자: " + str(self.author) + " 제목: "+self.title
