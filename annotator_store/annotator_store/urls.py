from django.conf.urls import patterns, include, url
from tastypie.api import Api
from store.api.resources import AnnotationResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(AnnotationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'annotator_store.views.home', name='home'),
    # url(r'^annotator_store/', include('annotator_store.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
