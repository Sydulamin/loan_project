from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'Enter valid e-mail address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Password Confirm'}))
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']