from django.conf.urls import patterns, url

from accounts.views.CreateAnAccount import CreateAnAccount
from accounts.views.LoginToAccount import LoginToAccount

urlpatterns = patterns('',
                       url(r'^logout/$', 'accounts.views.LogoutOfAccount.logout', name="logout"),
                       )
