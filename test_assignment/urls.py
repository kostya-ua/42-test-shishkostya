from django.conf.urls import patterns, include, url
from person.views import MainPageView
from utils.views import RequestsView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', MainPageView.as_view()),
     url(r'^requests/$', RequestsView.as_view()),
    # url(r'^test_assignment/', include('test_assignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
