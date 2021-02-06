from django.urls import path,include
from .auth import Login

urlpatterns = [
    #AUTH
    path('users/login',Login.as_view(),name = 'login'),
]