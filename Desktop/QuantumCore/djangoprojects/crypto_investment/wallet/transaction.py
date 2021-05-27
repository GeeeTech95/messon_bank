from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView
from django.views.generic.edit import CreateView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from urllib.parse import urlparse,urlunparse,urljoin
from .models import Wallet,WithdrawalApplication,Plan,PendingDeposit



class Deposit(LoginRequiredMixin,View)  :
    model = Wallet
    model_p = Plan
    template_name = 'deposit.html'

    def get(self,request,*args,**kwargs) :
        _slug = kwargs.get('slug',None)
        if not _slug : return HttpResponse("Invalid request")
        try : plan = self.model_p.objects.get(slug =_slug)
        except self.model_p.DoesNotExist :
            return HttpResponse("Plan you selected does not exist")
        return render(request,self.template_name,locals())

    def post(self,request,*args,**kwargs) :    
        return HttpResponse("Invalid")




class DepositComplete(LoginRequiredMixin,View)  :
    model = Wallet
    model_p = Plan
    template_name = 'deposit.html'

    def get(self,request,*args,**kwargs) :
        _slug = kwargs.get('slug',None)
        coin = kwargs.get('coin',None)
        if not _slug or not coin : return HttpResponse("Invalid request")
        try : plan = self.model_p.objects.get(slug =_slug)
        except self.model_p.DoesNotExist :
            return HttpResponse("Plan you selected does not exist")
        
        #check if user has pending deposit
        if not PendingDeposit.objects.filter(user = request.user,is_approved = False).exists() :
            #create pending deposit 
            PendingDeposit.objects.create(user = request.user,plan = plan,coin = coin) 
            url = urljoin(reverse('dashboard'),"?new=deposit") 
            return HttpResponseRedirect(url)
        else :
            return HttpResponse("You have a pending deposit already do wait for approval,thank You")    

    def post(self,request,*args,**kwargs) :    
        return HttpResponse("Invalid")




class Withdrawal(LoginRequiredMixin,View)  :
    model = WithdrawalApplication
    template_name = 'deposit.html'    
