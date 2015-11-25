# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# start tutorial
from django.core.exceptions import ValidationError
from djangular.forms import NgModelFormMixin
from . import forms 


class SignupForm(NgModelFormMixin,  forms.RegistrationForm):
    scope_prefix = 'subscribe_data'
    form_name = 'my_form'
    
    