from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^image_scraper/$', 'services.image_scraper.views.index'),
    (r'^admin/', include(admin.site.urls)),
)
