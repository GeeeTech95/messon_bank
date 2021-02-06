from django.urls import include,path
from .views import Index

urlpatterns = [
    path('',Index.as_view(),name ='index-ideal'),

]