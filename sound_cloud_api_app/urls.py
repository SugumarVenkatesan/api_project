from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
       url(r'^authenticate/',views.authenticate_soundcloud, name="authenticate_soundcloud"),
       url(r'^api_data/',views.get_api_details, name="soundcloud_api_data"),
)
