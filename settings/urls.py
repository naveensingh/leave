from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.LoginToAccount import LoginToAccount
from django.contrib.staticfiles import views

urlpatterns = patterns('',
                       url(r'^$', LoginToAccount.as_view(), name="index"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^account/',  include('accounts.urls')),
                       url(r'^profile/',  include('profiles.urls')),
                       url(r'^leave/',  include('leavebase.urls')),
                       url(r'^static/(?P<path>.*)$', views.serve),
                       )

urlpatterns += staticfiles_urlpatterns()
