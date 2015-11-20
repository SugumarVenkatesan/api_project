# from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm

# Create your views here.
class RegistrationView(TemplateView):
    template_name = 'contact_us/contact_us.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            print 'yes done'
            #save your model
            #redirect

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)

        form = RegistrationForm(self.request.POST or None)  # instance= None

        context["form"] = form
        #context["latest_article"] = latest_article

        return context