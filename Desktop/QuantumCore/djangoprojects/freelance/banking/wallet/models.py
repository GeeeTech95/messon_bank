from django.db import models
from django.contrib.auth import get_user_model
import random



class Wallet(models.Model) :
    
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name = 'wallet')
    transaction_pin = models.CharField(max_length=6,null = True)
    iban_number = models.CharField(max_length=30)
    otp = models.CharField(max_length=8,blank = True,null = True)
    balance = models.FloatField(default = 0.0)
    available_balance = models.FloatField(default = 0.0)
    #control spot
    allowed_to_transact = models.BooleanField(default=True)
    #when user is disaaalowed from maimg transactions
    disallow_reason = models.TextField(null = False,blank = True)
    is_frozen  = models.BooleanField(default = False)

    def __str__(self) :
        return self.user.username



class Transaction(models.Model) :
    def get_transaction_id(self) :
        PREFIX = "TD"
        number = random.randrange(10000000,999999999)
        number = PREFIX + str(number)
        if Transaction.objects.filter(transaction_id  = number).exists() : 
            self.get_transaction_id()
        return number

    TRANSACTION_TYPE = (('debit','DEBIT'),('credit','CREDIT'))
    TRANSACTION_NATURE  = (('withdrawal','WITHDRAWAL'),('deposit','DEPOSIT'),('transfer','TRANSFER'))
    STATUS = (('failed','FAILED'),('processing','PROCESSING'),('successful',"SUCCESSFUL"))
    
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,
    related_name = 'transaction')
    transaction_id = models.CharField(editable=False,null = False,max_length = 20)
    amount = models.FloatField()
    transaction_type = models.CharField(choices = TRANSACTION_TYPE,max_length= 10)
    nature = models.CharField(choices = TRANSACTION_NATURE,max_length= 12)
    status = models.CharField(choices = STATUS,max_length= 10)
    description = models.TextField()
    
    #if transfer
    receiver = models.ForeignKey(get_user_model(),related_name = 'transfer_receiver',on_delete = models.CASCADE)
    status_message = models.TextField()
    charge = models.FloatField(blank = True,default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs) :
        if not self.transaction_id :
            self.transaction_id = self.get_transaction_id()
        super(Transaction,self).save(*args,**kwargs)   

    def __str__(self) :
        return self.description[:20]