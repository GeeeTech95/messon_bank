from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.text import slugify


class Plan(models.Model) :
    name = models.CharField(max_length=40)
    slug = models.SlugField(blank = True)
    activation_cost = models.FloatField()   #in $usd
    duration = models.PositiveIntegerField()  #in days
    interest = models.FloatField()   #in $usd
    interest_rate = models.FloatField(blank = True)

    def __str__(self) :
        return self.name


    def save(self,*args,**kwargs) :
        self.slug = slugify(self.name)
        self.interest_rate = (self.interest/self.activation_cost)*100
        super(Plan,self).save(*args,**kwargs)

    class Meta() :
        ordering = ['-activation_cost']         


class Currency(models.Model) :
    name = models.CharField(max_length=10)

    def __str__(self) :
        return self.name

class Wallet(models.Model) :
    user = models.OneToOneField(get_user_model(),related_name = 'wallet_user',on_delete = models.CASCADE)
    preferred_currency = models.ForeignKey(Currency,related_name ='preferred_currency',on_delete = models.SET_DEFAULT,default = '1')
    plan = models.ForeignKey(Plan,related_name = 'active_plan',null = True,on_delete = models.SET_NULL)
    plan_start = models.DateTimeField(null = True)
    plan_end = models.DateTimeField(null = True)
    initial_balance = models.FloatField(default=0.0)  #for the plan
    set_amount = models.FloatField(blank = True,null = True)  #fadmin can set amount to override current balance calculation
    expected_maximum_balance = models.FloatField(default = 0.0) #at the end of the plan
    plan_is_active = models.BooleanField(default = False)

    @property
    def current_balance(self) :
        pass

    
    def __str__(self) :
        return self.user.username


class Transaction(models.Model) :
    t_choices = (('WITHDRAWAL','WITHDRAWAL'),('DEPOSIT','DEPOSIT'))
    coin_choices = (('BTC','BTC'),('USDT','USDT'),('ETH','ETH'),('BNB','BNB'))

    user  = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name = 'user_transaction')
    transaction_type = models.CharField(max_length=20,choices = t_choices)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    coin = models.CharField(max_length=10,choices = coin_choices)

class PendingDeposit(models.Model)    :
    user  = models.OneToOneField(get_user_model(),on_delete = models.CASCADE,related_name = 'user_pending_deposit')
    plan = models.ForeignKey(Plan,related_name = 'pending_deposits',null = True,on_delete = models.SET_NULL)
    is_approved  = models.BooleanField(default = False)
    coin = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.user.username




class WithdrawalApplication(models.Model) :
    coin_choices = (('BTC','BTC'),('USDT','USDT'),('ETH','ETH'),('BNB','BNB'))
    status = (('PENDING','PENDING'),('PROCESSING','PROCESSING'),('APPROVED','APPROVED'),('DECLINED','DECLINED'))
    user  = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name = 'user_withdrawal_ticket')
    amount = models.FloatField()  #in $
    coin = models.CharField(max_length=10,choices = coin_choices)
    wallet_address = models.CharField(max_length= 300)
    #extra address info goes here
    status = models.CharField(max_length= 20,choices = status)
    amount_paid = models.FloatField()  #in $ in case admin does not complete payment
    is_received = models.BooleanField(default = True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.user.username
    

 