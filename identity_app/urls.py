from django.conf.urls import patterns, url
from .views import RegistrationView,HomeView,LoginView,RegistrationConfirmView

urlpatterns = patterns('',
    url(r'^current_task/$', HomeView.as_view(), name="current_task"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^confirm/(?P<activation_key>\w+)/', RegistrationConfirmView.as_view() ,name="register_confirm"),
)





