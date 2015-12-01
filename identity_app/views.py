import json
import sys

from django.views.generic import TemplateView
from .forms.angular_forms import SignupForm, LoginForm
from .models import UserProfile
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.template import RequestContext

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class= SignupForm
    success_url = reverse_lazy('current_task')
    err_message = sys.exc_info()[1] 
    success_message = 'Successfully registered and the activation link has been sent to your mail'
    
    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super(RegistrationView, self).post(request, **kwargs)

    @transaction.atomic()
    def ajax(self, request):
        response_data = dict()
        form = self.form_class(data=json.loads(request.body))
        if form.is_valid():
            try:
                save_point = transaction.savepoint()
                form.save()
            except:
                transaction.savepoint_rollback(save_point)
                response_data.update({'error':self.err_message.message})
            else:
                transaction.savepoint_commit(save_point)
                response_data.update({'success':self.success_message})
        response_data.update({'errors': form.errors,'success_url': force_text(self.success_url)})
        return HttpResponse(json.dumps(response_data), content_type="application/json")

class RegistrationConfirmView(TemplateView):
    template_name = 'registration_confirm.html'
    err_message = sys.exc_info()[1]
    success_message = 'Your account was activated'
    activated_error_message = 'Your account was already activated'
    
    def get(self,request, *args, **kwargs):
        context = self.get_context_data()
        user_profile = get_object_or_404(UserProfile, activation_key=kwargs['activation_key'])
        user = user_profile.user
        if not user.is_active:
            try:
                save_point = transaction.savepoint()
                user.is_active = True
                user.save()
            except:
                transaction.savepoint_rollback(save_point)
                context.update({'error':self.err_message.message})
            else:
                context.update({'success':self.success_message})
        else:
            context.update({'error':self.activated_error_message})
        return super(TemplateView, self).render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super(RegistrationConfirmView, self).get_context_data(**kwargs)
        form = SignupForm()
        login_form = LoginForm()  # instance= None
        context["form"] = form
        context['login_form'] = login_form
        #context["latest_article"] = latest_article
        return context
    
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