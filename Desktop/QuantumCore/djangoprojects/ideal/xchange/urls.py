from django.urls import path,include
from .views import Index,Services,TOS,About,Contact
from .blog import News

urlpatterns = [
    path('',Index.as_view(),name = 'index-xchange'),
    path('about/',About.as_view(),name = 'about-xchange'),
    path('contact/',Contact.as_view(),name = 'contact-xchange'),
    path('news/',News.as_view(),name = 'news-xchange'),
    path('services/',Services.as_view(),name = 'services-xchange'),
    path('terms-of-service/',TOS.as_view(),name = 'tos-xchange'),    
    
]