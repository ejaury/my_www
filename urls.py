from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^image_downloader/$', 'services.image_downloader.views.index'),
    (r'^admin/', include(admin.site.urls)),
)
