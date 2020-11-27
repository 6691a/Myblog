from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    #path('singup/', singup, name='signup'),
    path('singup/', my_singup, name='signup'),
    path('activate/<str:uid64>/<str:token>', activate, name='activate')
]
