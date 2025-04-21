from .models import Grocery
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'quantity', 'price','image']   
        