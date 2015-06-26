from django.conf.urls import patterns, url
from profiles.Views.UpdatePersonalProfile import UpdatePersonalProfileView


urlpatterns = patterns('',
                       url(r'^edit', UpdatePersonalProfileView.as_view(), name="edit_profile"),
                       )
