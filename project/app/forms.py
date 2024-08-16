from django import forms
from django.forms import ModelForm
from .models import *

from .models import *

class ManagerForm(forms.ModelForm):
    phone=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','phone']

class EditManager_Form(forms.ModelForm):
    phone=forms.IntegerField(label='Phone No',widget=forms.TextInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone']



class GuestForm(forms.ModelForm):
    cpassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Reg_guest
        fields=['fullname','email','phone','password','cpassword','Adress']

class login_userForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput)

class ResortForm(forms.ModelForm):
    my_choice = (
        ('family','family'),
        ('friends','friends'),
        ('couple','couple'),
        ('comapnya_pack','company_pack'),
        ('get together','get together'),
        ('students pack','students pack'),
    )
    select_pack=forms.ChoiceField(choices=my_choice,widget = forms.Select(attrs={'class': 'form-control'}))

    # widget = forms.Textarea(attrs={'class': 'form-control ms-2', 'placeholder': 'Enter details'})
    class Meta:
        model=Resort_packs
        fields=['select_pack','price','details','no_of_rooms','img']













    





