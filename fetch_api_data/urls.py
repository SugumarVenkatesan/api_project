from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import home, settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fetch_api_data.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^f1/', include('f1_api_app.urls')),
    url(r'^soundcloud/', include('sound_cloud_api_app.urls')),
    url(r'^api/$', home.api_base_view, name="api_base_url"),
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="home"),   
)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )