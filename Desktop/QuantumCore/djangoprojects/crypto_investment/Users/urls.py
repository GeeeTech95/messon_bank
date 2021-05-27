from  django.urls import path,include
from .views import Subscribe
from .accounts import Register
from .dashboard import Dashboard,Profile

urlpatterns = [
    path('subscribe/',Subscribe.as_view(),name = 'subscribe'),
    path('register/',Register.as_view(),name = 'register'),
    path('dashboard/',Dashboard.as_view(),name = 'dashboard'),
    path('profile/',Profile.as_view(),name = 'profile'),


    #path('profile/',Profile.as_view(),name = 'register'),
    

]