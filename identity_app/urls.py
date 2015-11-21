from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import RegistrationView,HomeView

urlpatterns = patterns('',
    url(r'^current_task/$', HomeView.as_view(), name="current_task"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
)





