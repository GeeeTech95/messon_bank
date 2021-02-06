
from django.views.generic import View,TemplateView,DetailView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect

# Register your models here.

class Index(TemplateView) :
    template_name = 'index-ideal.html'