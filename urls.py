from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {
      'template_name': 'main/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name':'main/logout.html'}),
    ('^image_downloader/$', 'services.image_downloader.views.index'),
    (r'^admin/', include(admin.site.urls)),
)
