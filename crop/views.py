from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.http import *
from .models import Product
from .models import Customer
from django.views import generic
from django.views.generic import View
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# without the index(views/homepeg view)/view, the navbar wont show

class IndexView(generic.ListView):
	template_name = 'crop/index.html'



	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		# context['expenses'] = Expenses.objects.all()
		return context

	def get_queryset(self):
		return

class ProductListView(generic.ListView):
	template_name = 'crop/product.html'
	model = Product
	
	
	def get_context_data(self, **kwargs):
		context = super(ProductListView, self).get_context_data(**kwargs)
		context['product'] = Product.objects.all()
		return context
	def get_queryset(self):
		return Product.objects.all()


class CustomerListView(generic.ListView):
	template_name = 'crop/customer.html'
	model = Customer
	def get_context_data(self, **kwargs):
		context = super(CustomerListView, self).get_context_data(**kwargs)
		context['customer']=Customer.objects.all()
		return context
	def get_queryset(self):
		return Customer.objects.all()

class ProductDetailView(generic.DetailView):
	model = Product
	template_name = 'crop/product_detail.html'
	queryset = None

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', None)
		context['product'] = self.model.objects.get(pk=pk)
		return context
class CustomerDetailView(generic.DetailView):
	model = Customer
	template_name = 'crop/customer_detail.html'
	queryset = None

	def get_context_data(self, **kwargs):
		context = super(CustomerDetailView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', None)
		context['customer'] = self.model.objects.get(pk=pk)
		return context
class ProductCreate(CreateView):
	model = Product
	fields = ['product_name', 'category', 'cost', 'farm_name', 'country', 'city']
	success_url = ('/')
	
	def form_invalid(self, form):
		return http.HttpResponse("form is invalid")


	def form_invalid(self, form):
		return http.HttpResponse("form is invalid")
class CustomerCreate(CreateView):
	model = Customer
	fields = ['Customer_name', 'product', 'gender', 'contact', 'address', 'invoice_number ', 'other_details']
	success_url = ('success')

	def form_invalid(self, form):
		return http.HttpResponse("form is invalid")
		# caose stated here, delete below

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def main(request):
	...

 

		