from django.db import models
# enable to reverse yo code
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Product(models.Model):

	product_name = models.CharField(
		max_length=255,
		null=True,
		blank=True)
	# OperationalError: table crop_product has no column named category, means need to migrate 
	category_choices = (
		('Fruits', 'Fruits'),
		('Vegetables', 'Vegetables'),
		('Poultry', 'Poultry'),

		)
	category = models.CharField(
		max_length = 155,
		null = True,
		blank = True)

	quantity = models.CharField(max_length = 55, null = True, blank = True)

	cost = models.CharField(
		max_length = 255,
		null = True, 
		blank = True)

	manufactured = models.DateTimeField(
		max_length = 255,
		null = True,
		blank = True)
	# expiry date field (default= None,  null=True, blank=True)
	expiry_date = models.DateTimeField(default= None,  null=True, blank=True)

	timestamp = models.DateTimeField(auto_now_add = True)
	
	farm_name = models.CharField(
		max_length = 255,
		null = True,
		blank = True)
	country_choices = (
		('ZM', 'Zambia'),
		('MX', 'Mexico'),
		('SA', 'South Africa')
		)
	country = models.CharField(max_length = 255, null = True, blank =True)

	city = models.CharField(
		max_length=255,
		null=True,
		blank=True)
	customer_email= models.CharField(
		max_length= 255, 
		null = True, 
		blank = True)

	def __str__(self):
			return self.product_name

	
 				# wana make this a form for +customer order, how cn it be?
class Customer(models.Model):
		customer_name = models.CharField(
			max_length = 155,
			null = True,
			blank =  True)
		# onc
		product = models.ForeignKey(Product, on_delete=models.CASCADE)
		
		gender_choices = (
			('Male', 'Male'),
			('Female', 'Female'),
			('State_Other', 'State_Other'),
			)
		gender = models.CharField(max_length = 6, null = True, blank = True)

		cost = models.CharField(max_length = 55, null = True, blank = True)

		contact= models.CharField(
			max_length  =255,
			null = False,
			blank = False)
		address = models.TextField(
			null=True,
			blank=True)
		invoice_number = models.CharField(
			max_length = 55,
			null = True,
			blank = True)

		other_details = models.TextField(
			'Other Details',
			null=True,
			blank=True)
		
		def __str__(self):
			return self.customer_name


	
