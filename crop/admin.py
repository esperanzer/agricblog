from django.contrib import admin
# Register your models here
from .models import Product, Customer

# if u jst register yo models like this"admin.site.register(Product) tables wont be smart" in d admin site



class ProductAdmin(admin.ModelAdmin):

	list_display = ['product_name', 'category', 'quantity', 'cost', 'manufactured', 
	'farm_name', 'city', 'country', 'expiry_date']

admin.site.register(Product, ProductAdmin)
	


class CustomerAdmin(admin.ModelAdmin):
	list_display = ['customer_name', 'gender', 'product', 'cost', 'invoice_number', 'address', 'contact', 'other_details']
admin.site.register(Customer, CustomerAdmin)
		
		