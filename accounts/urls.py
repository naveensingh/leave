from django.conf.urls import patterns, url

from accounts.views.CreateAnAccount import CreateAnAccount
from accounts.views.LoginToAccount import LoginToAccount

urlpatterns = patterns('',
                       url(r'^create$', CreateAnAccount.as_view(), name="signup"),
                       url(r'^login$', LoginToAccount.as_view(), name="login"),
                       url(r'^logout/$', 'accounts.views.LogoutOfAccount.logout', name="logout"),
                       )
