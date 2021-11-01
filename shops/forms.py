from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from .models import ShopProfile
from django.core.mail import send_mail
from datetime import datetime
from django.core import validators
from django.contrib import messages
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class ShopProfileForm(forms.ModelForm):
    
    class Meta:
        model = ShopProfile
        fields = ("title","shop_address","shop_bg","shop_category","city","description","facebook","twitter","pinterest","instagram","youtube")
      

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'shop_address' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ShopProfileForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['shop_category'].widget.attrs['readonly'] = True
            self.fields['title'].widget.attrs['readonly'] = True
         