from . import forms
from django.shortcuts import render,render_to_response,RequestContext
from fetch_api_data.forms import APIListForm

def api_base_view(request):
    args = {}
    args['form'] = APIListForm()
    return render_to_response('base.html', args, context_instance=RequestContext(request)) 