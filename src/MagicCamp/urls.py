# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from views import  *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^MagicCamp/', include('MagicCamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/', hello),
    (r'^time/',cur_dt),
    #(r'^$',lambda : return "Hi"),
)

