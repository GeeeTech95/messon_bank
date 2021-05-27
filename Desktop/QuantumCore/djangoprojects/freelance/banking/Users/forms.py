from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User



class UserCreateForm(UserCreationForm) :
  
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = UserCreationForm.Meta.fields + ('username','email','country','state','address','phone_number','occupation','passport','date_of_birth')


class ProfileUpdateForm(ModelForm) :
    class Meta() :
        model  = User
        fields = ['phone_number']
