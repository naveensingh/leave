from django.conf.urls import patterns, url
from landing.DefaultAppLanding import LandingView

urlpatterns = patterns('',
                       url(r'^dashboard/$', LandingView.as_view(), name="dashboard"),
                       )
