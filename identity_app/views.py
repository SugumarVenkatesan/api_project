# from django.shortcuts import render
import json

from django.views.generic import TemplateView
from .forms.angular_forms import SignupForm 
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from django.core.urlresolvers import reverse_lazy

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class= SignupForm
    success_url = reverse_lazy('current_task')
    
    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(RegistrationView, self).post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
    
class HomeView(TemplateView):
    template_name = 'id_homepage.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return super(TemplateView, self).render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        form = SignupForm(self.request.POST or None)  # instance= None

        context["form"] = form
        #context["latest_article"] = latest_article

        return context