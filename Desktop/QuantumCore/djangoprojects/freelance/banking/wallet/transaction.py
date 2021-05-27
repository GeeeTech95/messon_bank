
class Transaction() :
    def __init__(self,user) :
        self.user = user



    def credit(self,amount,user=None)  :
        if not user : user = self.user
        wallet = user.wallet
        wallet.available_balance += amount 
        wallet.save()
        #ensure it added
        return
            

    def debit(self,amount,user=None) :
        if not user : user = self.user
        wallet = user.wallet
        wallet.available_balance -= amount 
        wallet.save()
        #ensure it added
        return

    def internal_transfer(self,receipient,amount) :
        try :
            self.debit(amount)
            self.credit(amount=amount,user= receipient)
            state = 0
        except :
            state =   "An Error occured"    
        return state





