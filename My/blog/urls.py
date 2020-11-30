from django.urls import path, include
from .views import *


app_name = 'post'
urlpatterns = [
    # path('', postView, name="posts"),
    # path('detail/<int:pk>', postDetailView, name="postDetail"),
    path('addpost/', addPostView, name="add_post"),
    path('', post_in_category, name='post_all'),
    path('<str:category_slug>/', post_in_category, name='post_in_category'),
    path('<str:post_slug>/<int:id>/', post_detail, name='post_detail'),

]
