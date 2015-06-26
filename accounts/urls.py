from django.conf.urls import patterns, url

from accounts.CreateAnAccount import CreateAnAccount
from accounts.LoginToAccount import LoginToAccount

urlpatterns = patterns('',
                       url(r'^create$', CreateAnAccount.as_view(), name="signup"),
                       url(r'^login$', LoginToAccount.as_view(), name="login"),
                       url(r'^logout/$', 'accounts.LogoutOfAccount.logout', name="logout"),
                       )
