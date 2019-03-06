 # if your STATIC_URL is defined as /static/, you can do 
 # this by adding  the following snippet to your urls.py:

from django.conf.urls import url
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from .models import Product, Customer 
from .views import Product, Customer
# d two lines belo ar 
from django.contrib import admin
from django.contrib.auth import views as auth_views



from . import views

app_name = "crop"

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^product/', views.ProductListView.as_view(), name='product'),
  url(r'^customer/', views.CustomerListView.as_view(), name='customer'),
  url(r'^about_us/', views.ProductListView.as_view(), name='about_us'),
  url(r'^product_detail/(?P<pk>\d+)/detail/', views.ProductDetailView.as_view(), name = 'product_detail'),
  url(r'^customer_detail/(?P<pk>\d+)/detail/', views.CustomerDetailView.as_view(), name = 'customer_detail'),
  url(r'^orders-add/$', views. ProductCreate.as_view(), name = 'orders-add'),
  # url(r'^customer-add/$', views. CustomerCreate.as_view(), name = 'customer-add'),
   url(r'^login/$', auth_views.login, name='login'),
   url(r'^logout/$', auth_views.logout, name='logout'),
   url(r'^admin/', admin.site.urls),


]
