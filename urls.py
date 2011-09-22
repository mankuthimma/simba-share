from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^smbshare/', include('smbshare.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^manager/$', 'smbshare.manager.views.index'),
    (r'^manager/index$', 'smbshare.manager.views.index'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/shashi/projects/smbshare/media'}),
    (r'^manager/form$', 'smbshare.manager.views.form'),
    (r'^manager/add$', 'smbshare.manager.views.add'),
    (r'^manager/(?P<sharename>.+)/remove$', 'smbshare.manager.views.remove'),
    (r'^manager/(?P<sharename>.+)/edit$', 'smbshare.manager.views.edit'),
    (r'^manager/modify$', 'smbshare.manager.views.modify'),
)
