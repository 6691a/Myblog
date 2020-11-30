from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ['name']}

# @admin.register(Post)
# class CategoryAdmin(admin.ModelAdmin):


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'slug', 'display']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
