import soundcloud

from django.shortcuts import render,render_to_response,RequestContext
from django.conf import settings
from django.http import HttpResponse
from django.core.context_processors import csrf
from fetch_api_data.forms import *
from .services import SoundCloudApiFactory
from django.contrib import messages
from django.http.response import HttpResponseRedirect

def authenticate_soundcloud(request):
    api_connection = SoundCloudApiFactory()   
    return HttpResponseRedirect(api_connection.get_authorize_url()+'&display=popup')

def get_api_details(request):
    import pdb;pdb.set_trace()
    api_connection = SoundCloudApiFactory()
    return HttpResponseRedirect('/')