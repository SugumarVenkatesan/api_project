from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^api_data/',views.f1_api_data, name="f1_api_data"),
)
