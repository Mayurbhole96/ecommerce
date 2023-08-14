from django import forms
from django.forms import ModelForm
from .models import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title','details','attached_files','price','seller']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product_id','buyer','seller']
