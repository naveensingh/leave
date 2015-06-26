from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from landing.DefaultAppLanding import LandingView

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', LandingView.as_view(),
                           name="index"),
                       )

urlpatterns += staticfiles_urlpatterns()
