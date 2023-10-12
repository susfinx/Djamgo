from django import forms
from .models import Product, Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone_number', 'address',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity','image')

# class OrderForm(forms.ModelForm):
#    class Meta:
#        model = Order()
#        fields = ['client', 'products', 'total_amount']
