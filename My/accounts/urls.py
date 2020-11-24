from django.urls import path
from .views import *

urlpatterns = [
    path('logint/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('singup/', signup, name='signup'),
    #path('activate/<str:uid64>/<str:token>', name='activate')
]
