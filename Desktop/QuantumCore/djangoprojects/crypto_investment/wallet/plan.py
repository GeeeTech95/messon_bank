from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView
from django.views.generic.edit import CreateView,UpdateView
from .models import Plan,Wallet

class PlanList(ListView) :
    model = Plan
    template_name = 'plan-list.html'
    context_object_name  = 'plans'


class ChoosePlan(RedirectView) :
    """
    returns  to payment page with required data
    """







