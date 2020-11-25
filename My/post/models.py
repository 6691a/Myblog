from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # 작성자를 포린키(유저)로 설정 유저가 사라지면 작성 글 또한 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    # admin 노출될 형식
    class Meta:
        db_table = 'posts'

    def __str__(self):
        return "작성자: " + str(self.author) + " 제목: "+self.title
