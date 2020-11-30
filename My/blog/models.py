from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, db_index=True)
    # pk 대신 접근을 위한 값
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True, allow_unicode=True, default=' ')
    # 검색 엔진에 노출될 설명
    meta_description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        db_table = 'category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:post_in_category', args=[self.slug])

        # return reverse('post_in_category', args=[self.slug])


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # 작성자를 포린키(유저)로 설정 유저가 사라지면 작성 글 또한 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True, allow_unicode=True, default=' ')
    # related_name -> setPost로 불러올 수 잇지만 좀 더 쉽게 만듬
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    display = models.BooleanField(default=True)

    # admin 노출될 형식
    class Meta:
        db_table = 'post'
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return "작성자: " + str(self.author) + " 제목: "+self.title

    def get_absolute_url(self):
        # return reverse('post_detail', args=[self.slug, self.id])

        return reverse('post:post_detail', args=[self.slug, self.id])
