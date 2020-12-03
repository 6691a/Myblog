from django.urls import path, include
from .views import *


app_name = 'post'
urlpatterns = [
    # path('', postView, name="posts"),
    # path('detail/<int:pk>', postDetailView, name="postDetail"),
    path('addpost/', addPostView, name="add_post"),
    path('', post_page_category, name='post_all'),
    path('category/<str:category_slug>/',
         post_page_category, name='post_in_category'),
    path('detail/<str:post_slug>/<int:id>/',
         post_detail, name='post_detail'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
    path('update/<str:post_slug>/<int:id>/', post_update, name='post_update'),
]
