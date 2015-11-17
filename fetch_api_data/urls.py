from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fetch_api_data.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^f1/', include('f1_api_app.urls')),
    url(r'^soundcloud/', include('sound_cloud_api_app.urls')),
    url(r'^$', home.api_base_view, name="base_url"),
)


urlpatterns += staticfiles_urlpatterns()