from django.conf.urls import include, url   
from django.contrib import admin
# from django.http import HttpResponseRedirect
# importing app urls
from crop import urls as crop_urls
# importing views, bt u cn coment out d below lin 4view wl stil work
from django.contrib.auth import views

app_name = 'crop'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # d below line wek 2gether wth d 4th line on top
    url(r'^crop/', include(crop_urls, namespace = 'crop')),
    # url(r'^main/$', 'login.views.main'),
    # (r'^login/$', 'crop.views.login_user'),

  
]


