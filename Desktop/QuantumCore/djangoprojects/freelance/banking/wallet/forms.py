from django import forms
from .models import Wallet
from django.contrib.auth import get_user_model


class InbankTransferForm(forms.Form) :
    account_number = forms.CharField()
    amount = forms.FloatField()
    description = forms.TextInput()


    def clean_account_number(self) :
        acc_num = self.cleaned_data['account_number']  
        if not get_user_model().objects.filter(account_number = acc_num).exists() :
            raise forms.ValidationError("The entered account number does not belong to any valid account")
        return acc_num

        


