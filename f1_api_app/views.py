from django.shortcuts import render,render_to_response,RequestContext
from django.conf import settings
from django.http import HttpResponse
from django.core.context_processors import csrf
from fetch_api_data.forms import *
from .services import APIService
from django.contrib import messages

api_params = {'offset':0,'limit':3}

def f1_api_data(request):
    args = {}
    args.update(csrf(request))
    args['has_next'] = True
    args['has_previous'] = False
    if request.method == 'POST':
        form = APIListForm(request.POST)
        args['form'] = form
        if form.is_valid():
            try: 
               api_url = form.cleaned_data['api_list']
               if 'args' in request.GET and request.GET['args']=='next':
                   api_params['offset'] += api_params['limit']
               if 'args' in request.GET and request.GET['args']=='previous':
                   if api_params['offset'] > 0:
                       api_params['offset'] -= api_params['limit']
                   args['has_next'] = True
               if api_params['offset'] > 0:
                   args['has_previous'] = True
               api_instance = APIService(api_url,api_params)
               api_data = api_instance.f1_api_services()
            except IndexError:
                api_params['offset'] = 0
                api_params['limit'] = 3
                api_instance.api_params = api_params
                api_data = api_instance.f1_api_services() 
                args['api_data'] = api_data
                args['has_previous'] = False
            except Exception,e:
                messages.add_message(request,messages.ERROR,e.message)
                args['has_next'] = False
                args['has_previous'] = False
            else:             
                args['api_data'] = api_data      
    else:
        args['has_next'] = False
        args['has_previous'] = False
        args['form'] = APIListForm()
    return render_to_response('f1_app.html', args, context_instance=RequestContext(request))


