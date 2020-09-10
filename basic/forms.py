from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  *


class RegisterForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]


class EmpForm(forms.ModelForm):
    
    
    
    class Meta:
        model = Profile
        
        fields = ["name","phone","email","password","image"]        