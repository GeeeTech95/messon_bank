from django.urls import reverse_lazy,reverse
from django.shortcuts import render
from django.views.generic import CreateView,View
from .models import  User
from .forms import UserCreateForm

class Register(CreateView) :
    template_name = 'register.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('login')


    