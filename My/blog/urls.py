from django.urls import path
from .views import *

urlpatterns = [
    path('', postView, name="posts"),
    path('detail/<int:pk>', postDetailView, name="postDetail"),
    path('addpost/', addPostView, name="addPost"),

]
