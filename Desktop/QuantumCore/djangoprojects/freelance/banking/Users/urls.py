from  django.urls import path,include
from .accounts import Register
from .dashboard import Dashboard,Profile

urlpatterns = [
    path('',Dashboard.as_view(),name = 'dashboard'),
    path('create/',Register.as_view(),name = 'register'),
    path('info/',Profile.as_view(),name = 'profile'),


]