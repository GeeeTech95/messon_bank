from django.urls import path,include
from .auth import Login
from .blog import BlogDetail

urlpatterns = [
    #AUTH
    path('users/login',Login.as_view(),name = 'login'),


    #BLOG
    path('blog/<slug:slug>/',BlogDetail.as_view(),name = 'blog-detail-core')
]