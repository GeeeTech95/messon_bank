from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from core.views import Notification
from .forms import TransferForm,PinForm
from .models import Wallet,Transaction as transaction_model
from .helpers import Transaction

import time


class CompleteTransaction(LoginRequiredMixin,UserPassesTestMixin,View) :
    """
    this handles completeing ttransaction which were incomplete for one reason or the other
    using transaction id and making sure pin matches and user is owner of transaction"""
    feedback = {}
    transaction = None
    form_class  = PinForm
    template_name = 'enter-pin.html'
    
    def get(self,request,*args,**kwargs) :
        
        account = request.user.wallet
        if not account.allowed_to_transact :
            response = request.user.wallet.disallow_reason or ""
            return HttpResponse(response) 
        form =  self.form_class
        transact_id = kwargs['transact_id']
        try : 
            transact = transaction_model.objects.get(transaction_id = transact_id)        
            if transact.status == 'Successful' :
                return HttpResponse('This transaction has been processed completely')
        except : return HttpResponse("Invalid request")
        
            
        return render(request,self.template_name,locals())



    def post(self,request,*args,**kwargs) :
        self.feedback = {}
        form = self.form_class(request.POST)
        if form.is_valid() :
            #check pin match
            pin = form.cleaned_data['pin']
            if not pin == request.user.wallet.transaction_pin :
                self.feedback['error'] = "The Pin You entered is incorrect,please try again !"
                return JsonResponse(self.feedback)

            if not request.user.wallet.allowed_to_transact :
                self.feedback['error'] =  request.user.wallet.disallow_reason or ""
                return JsonResponse(self.feedback) 

            transact = Transaction(request.user)
            if self.transaction.nature == 'Internal Transfer' :
                #making sure the transaction is not processed already
                if  not self.transaction.status == 'Successful' :
                    state = transact.internal_transfer(self.transaction.receiver,self.transaction.amount)
                    if  state == 0 :
                        self.feedback['success'] = True
                        msg = "Your transfer of {} to {},acc ******{} was successful".format(
                            self.transaction.amount,
                            self.transaction.receiver,
                            self.transaction.receiver.account_number[6:]
                        )
                        #send mail
                        #send message
                        Notification.notify(request.user,msg)
                        self.transaction.status = 'Successful'
                        self.transaction.status_message = "TRF ${}  to  {},Acc ******{} ".format(
                            self.transaction.amount,
                            self.transaction.receiver,
                            self.transaction.receiver.account_number[6:]
                        )
                        self.transaction.save()
                    else :
                        self.feedback['error'] =  state 
                        return JsonResponse(self.feedback)
                else :
                    self.feedback['error'] = 'This transaction has been processed completely'
            
            else :
                if  not self.transaction.status == 'Successful' :
                    state = transact.external_transfer(self.transaction.amount)
                    if  state == 0 :
                        self.feedback['success'] = True
                        msg = "Your transfer of {} to {},acc ******{} was successful".format(
                            self.transaction.amount,
                            self.transaction.account_name,
                            self.transaction.account_number[6:]
                        )
                        #send mail
                        #send message
                        Notification.notify(request.user,msg)
                        self.transaction.status = 'Successful'
                        self.transaction.status_message = "TRF ${}  to  {},Acc ******{} ".format(
                            self.transaction.amount,
                            self.transaction.account_name,
                            self.transaction.account_number[6:]
                        )
                        self.transaction.save()
                    else :
                        self.feedback['error'] =  state 
                        return JsonResponse(self.feedback)
                else :  
                    self.feedback['error'] = 'This transaction has been processed completely'
                return JsonResponse(self.feedback)

             



        else :
            self.feedback['error'] = 'yellow'
            return JsonResponse(self.feedback) 
            
        return JsonResponse(self.feedback)          

    def test_func(self) :
        transact_id = self.kwargs['transact_id']
        try : transaction = transaction_model.objects.get(transaction_id = transact_id)        
        except : return False
        #THE TRANSACTION OBJECT
        self.transaction = transaction
        return transaction.user == self.request.user


class Deposit(LoginRequiredMixin,View) :
    pass


class Transfer(LoginRequiredMixin,View) :

    template_name = 'transfer.html'
    form_class = TransferForm
    model2 = Wallet 
    model = get_user_model

    #for swift_number,first 4 is for bank code,next 2 is country,next two is state/city code,
    #optional 3 for branch
    allowable_transaction = [

        {
        'account_name' : 'Isaac chruchill',
        'iban' : 'AU46284928482329475455',
        'swift_number' : 'CBAMAUSD',
        'bic' : 'RF34874873484',
        'account_number' : '348904772848',
        'bank_name' : 'Continental Bank',
        'country' : 'Australia', 
        },

        {
        'account_name' : 'Joan Elizabeth',
        'iban' : 'DE94100110012620776617',
        'bic' : 'RF34874873484',
        'swift_number' : 'NTSBDEBC',
        'account_number' : '348904772848',
        'bank_name' : 'Local Gigo Bank',
        'country' : 'Denmark', 
        }

    ]

    def get(self,request,*args,**kwargs) :
        account = request.user.wallet
        form =  self.form_class
        return render(request,self.template_name,locals())

    def post(self,request,*args,**kwargs) :
        form = self.form_class(request.POST) 
        if form.is_valid() :
            acc_num = form.cleaned_data['account_number'] 
            amount = form.cleaned_data['amount']
            transact_type = form.cleaned_data['transfer_type']
            #if internal
            receipient = None
            if  transact_type == 'Internal Transfer' :
                receipient = get_user_model().objects.get(account_number = acc_num)
            

            else :
                """ check if details match for international transfer """
                if transact_type != "Internal Transfer"  :
                    iban = form.cleaned_data['iban']
                    bic = form.cleaned_data['bic']
                    swift_number = form.cleaned_data.get('swift_number',None)
                    #check if details is in our list,else give network error
                    details,error = None,None
                    for info in self.allowable_transaction :
                        if info['account_number'] ==  acc_num :
                            #checking if other details match
                            if  info['iban'] == iban and info['bic'] == bic :
                                #swift can be empty
                                if swift_number and info['swift_number'] == swift_number :
                                    details = info
                                else :
                                    error = "Data Mismatch !,swift number does not match account number info,please crosscheck !"    
                            else :
                                error = "Data Mismatch !,Entered data does not match account number info,please crosscheck !"
                                
                    #assuming no match
                    if not details :
                        time.sleep(2)
                        error = error or "Request Time Out,please Try again later"
                        return render(request,self.template_name,locals())
            #check if user has the amount
            if not request.user.wallet.available_balance >  float(amount) :
                error = "Insufficient Funds,Enter a lower amount"
                return render(request,self.template_name,locals())
            else :

                #create transaction,but its still pending because of pin issues
                if details :
                    acc_name = details['account_name']
                    bank_name = details['bank_name']
                    country = details['country']
                else :
                    acc_name,bank_name,country = None,None,None

                transact = transaction_model.objects.create(
                    user = request.user,
                    amount = amount,
                    transaction_type = 'Debit',
                    nature = form.cleaned_data['transfer_type'],
                    description = form.cleaned_data['description'],
                    status = "Processing",
                    status_message  = "Waiting for Transaction Pin Authorization",
                    receiver  = receipient,
                    swift_number = form.cleaned_data.get('swift_number',None),
                    iban =  form.cleaned_data.get('iban',None),
                    bic =  form.cleaned_data.get('bic',None),
                    account_number =  acc_num,
                    account_name = acc_name,
                    country = country,
                    bank_name = bank_name
                )
                return HttpResponseRedirect(reverse('complete-transaction',args=[transact.transaction_id]))    
        else :
            return render(request,self.template_name,locals())     
            




