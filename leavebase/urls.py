from django.conf.urls import patterns, url
from leavebase.views.AllLeaves import ListOfAllAppliedLeaves

from leavebase.views.LeaveBaseFormView import ApplyForLeaveView


urlpatterns = patterns('',
                       url(r'^apply/$', ApplyForLeaveView.as_view(), name="apply_for_leave"),
                       url(r'^all/$', ListOfAllAppliedLeaves.as_view(), name="list_of_all_applied_leaves"),
                       )
