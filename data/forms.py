from django import forms
from django.forms import ModelForm
from . models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields= '__all__'
        # widgets ={
        #     'customer' : forms.Select(attrs={'class' : 'form-control'}),
        #     'product' : forms.Select(attrs={'class' : 'form-control'}),
        #     'status' : forms.Select(attrs={'class' : 'form-control'}),
        # }
        # labels = {
        #     'customer' : 'Konsumen',
        #     'product' : 'Produk',
        #     'status' : 'Status Order',
        # }