from django.conf.urls import patterns, url
from landing.DefaultAppLanding import LandingView

urlpatterns = patterns('',
                       url(r'^$', LandingView.as_view(),
                           name="index"),
                       )
