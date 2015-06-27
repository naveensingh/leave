from django.conf.urls import patterns, url

from profiles.Views.UpdatePersonalProfile import UpdatePersonalProfileView
from profiles.Views.ViewPersonalProfile import PersonalProfileView

urlpatterns = patterns('',
                       url(r'^edit/(?P<profile_slug>.*)/$', UpdatePersonalProfileView.as_view(), name="edit_profile"),
                       url(r'^(?P<profile_slug>.*)/$', PersonalProfileView.as_view(), name="view_profile"),
                       )
