import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from leavebase.models import LeaveBase

from django.contrib.messages import error
from django.utils.translation import ugettext_lazy as _


class ApproveLeaveRequestView(View):
    template_name = 'leave/list_of_all_unapporved_leave_requests.html'
    model = LeaveBase

    def setup(self):
        self.request_type = self.request.GET.get('status', None)
        if self.request_type == "open":
            self.get_all_leave_requests = LeaveBase.objects.filter(is_approved=False)
            self.title = "All open leave requests"
        elif self.request_type == "approved":
            self.get_all_leave_requests = LeaveBase.objects.filter(is_approved=True)
            self.title = "All approved leave requests"
        else:
            self.get_all_leave_requests = None
        self.get_user_with_permission = self.request.user_profile.can_approve

    def get_context(self):
        return {
            "list_of_all_applied_leaves": self.get_all_leave_requests,
            "title": self.title,
            "page_id": "list_of_all_applied_leaves"
        }

    @method_decorator(login_required)
    def get(self, request):
        self.setup()
        if self.get_user_with_permission:
            context = self.get_context()
            return render(request, self.template_name, context)
        else:
            error(self.request, _("You do not have permission"))
            return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form_data = request.POST
        leave_id = form_data.get('leave_id')
        is_approved = form_data.get('is_approved')
        try:
            leave_approval = LeaveBase.objects.get(id=leave_id)

            if is_approved == "true":
                leave_approval.is_approved = True

            if is_approved == "false":
                leave_approval.is_approved = False

            leave_approval.save()
            return HttpResponse(json.dumps({"message": "Leave Approved Sucessfully"}),
                                content_type="application/json")
        except Exception as ex:
            print ex
            return HttpResponse(json.dumps({"message": "Something went wrong..."}), content_type="application/json")
