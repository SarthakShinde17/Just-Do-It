from .models import Grocery
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
  
        