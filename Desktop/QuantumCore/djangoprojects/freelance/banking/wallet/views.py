from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .forms import InbankTransferForm
from .models import Wallet,Transaction
from .transaction import Transaction


class CompleteTransaction(LoginRequiredMixin,UserPassesTestMixin,View) :
    """
    this handles completeing ttransaction which were incomplete for one reason or the other
    using transaction id and making sure pin matches and user is owner of transaction"""
    feedback = {}
    transaction = None
    
    def get(self,request,*args,**kwargs) :
        template_name = 'enter-pin.html'
        account = request.user.wallet
        form =  self.form_class
        transact_id = kwargs['transact_id']
        try : transaction = Transaction.objects.get(transaction_id = transact_id)        
        except : return HttpResponse("Invalid request")
        return render(request,self.template_name,locals())


    def post(self,request,*args,**kwargs) :
        transact = Transaction(request.user)
        if self.transaction.transaction_type == 'internal_transfer' :
            state = transact.internal_transfer(self.tansaction.receiver,self.tansaction.amount)
            if  state == 0 :
                self.feedback['success'] = True
                
            else :
                self.feedback['error'] =  state 
        elif False :
            pass
        return JsonResponse(self.feedback)          

    def test_func(self) :
        transact_id = self.kwargs['transact_id']
        try : transaction = Transaction.objects.get(transaction_id = transact_id)        
        except : return False
        #THE TRANSACTION OBJECT
        self.transaction = transaction
        return transaction.user == self.request.user

class Deposit(LoginRequiredMixin,View) :
    pass


class Transfer() :
    class InBank(LoginRequiredMixin,View) :
        template_name = 'transaction-form.html'
        form_class = InbankTransferForm
        model2 = Wallet 
        model = get_user_model

        def get(self,request,*args,**kwargs) :
            account = request.user.wallet
            form =  self.form_class
            return render(request,self.template_name,locals())

        def post(self,request,*args,**kwargs) :
            form = self.form_class(request.POST) 
            if form.is_valid() :
                acc_num = form.cleaned_data['account_number'] 
                amount = form.cleaned_data['amount']
                receipient = get_user_model().objects.get(account_number = acc_num)
                #check if user has the amount
                if not user.wallet.available_balance >  float(amount) :
                    error = "Insufficient Funds,Enter a lower amount"
                    return render(request,self.template_name,locals())
                else :
                    #create transaction,but its still pending beause of pin issues
                    transact = Transaction.objects.create()
                    return HttpResponseRedirect(reverse('complete-transaction',args=[transact.transaction_id]))    
            else :
                return render(request,self.template_name,locals())     
                




