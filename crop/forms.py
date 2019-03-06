from django import forms
# from django.contrib.auth.models import User
from .models import Product, Customer




class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['product_name', 'category', 'cost', 'farm_name', 'country ', 'city']



class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['Customer_name', 'product', 'gender', 'contact', 
		'address', 'invoice_number', 'other_details']
	
