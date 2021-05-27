from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView,TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from wallet.models import Wallet,WithdrawalApplication
from .forms import ProfileUpdateForm


class Dashboard(TemplateView) :
    template_name = 'dashboard.html'


class Profile(LoginRequiredMixin,UpdateView) :
    template_name = 'profile.html'
    model = get_user_model()
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('dashboard')
    
    def get_object(self) :
        return self.request.user

    def get(self,request,*args,**kwargs) :
        form = self.form_class(initial = model_to_dict(request.user))
        return render(request,self.template_name,locals())

