# from django.shortcuts import render
import json

from django.views.generic import TemplateView
from .forms.angular_forms import SignupForm, LoginForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class= SignupForm
    success_url = reverse_lazy('current_task') 
    
    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(RegistrationView, self).post(request, **kwargs)

    def ajax(self, request):
        response_data = dict()
        form = self.form_class(data=json.loads(request.body))
        if form.is_valid():
            try:
                form.save()
            except:
                response_data.update({'error':'An Error Occured'})
            else:
                response_data.update({'success':'Successfully registered'})
        response_data.update({'errors': form.errors,'success_url': force_text(self.success_url)})
        return HttpResponse(json.dumps(response_data), content_type="application/json")

class LoginView(FormView):
    template_name = 'login.html'
    form_class= LoginForm
    success_url = reverse_lazy('current_task')
    
    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(LoginView, self).post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body))
        if form.is_valid():
            try:
                pass
            except:
                pass
            else:
                pass
        response_data = {'errors': form.errors,'success_url': force_text(self.success_url)}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
class HomeView(TemplateView):
    template_name = 'id_homepage.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return super(TemplateView, self).render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = SignupForm()
        login_form = LoginForm()  # instance= None
        context["form"] = form
        context['login_form'] = login_form
        #context["latest_article"] = latest_article
        return context