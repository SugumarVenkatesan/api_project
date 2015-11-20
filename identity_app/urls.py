from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^current_task/$', TemplateView.as_view(template_name='id_homepage.html'), name="current_task"),
)





