# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# start tutorial
from django.core.exceptions import ValidationError
from djangular.forms import NgModelFormMixin
from . import forms 


class SignupForm(NgModelFormMixin,  forms.RegistrationForm):
    scope_prefix = 'subscribe_data'
    form_name = 'my_form'
    
class LoginForm(NgModelFormMixin,  forms.AuthenticationForm):
    scope_prefix = 'login_data'
    form_name = 'login_form'
    
#     def clean(self):
#         if self.cleaned_data.get('username') and self.cleaned_data.get('password'):
#             raise ValidationError('Invalid Credentials')
#         return super(LoginForm,self).clean()
#         cleaned_data = super(LoginForm, self).clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         if username and password:
#             try:
#                 user = authenticate(username = username,password= password)
#                 if user is None:
#                     raise Exception
#             except Exception:
#                 raise forms.ValidationError('Invalid Credentials')
#             else:
#                 return user
#         return super(L)