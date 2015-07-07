from django.conf.urls import patterns, url

from leavebase.views.LeaveBaseFormView import ApplyForLeaveView


urlpatterns = patterns('',
                       url(r'^apply/$', ApplyForLeaveView.as_view(), name="apply_for_leave"),
                       )
