from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,password_validation,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer

class UserRegistration(UserCreationForm):
    email=forms.CharField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  

    class Meta:
        model=User
        fields=['username', 'email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # class Meta:

    #     model=User
    #     # fields=['username', 'password']
    #     # widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),strip=False,
     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control', "autofocus": True}))
    new_password1 = forms.CharField(label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),strip=False,
        help_text=password_validation.password_validators_help_text_html(), )
    new_password2 = forms.CharField(label=("New password confirmation"), strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )

class MyPasswordResetForm(PasswordResetForm):
     email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control'}),
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})}
