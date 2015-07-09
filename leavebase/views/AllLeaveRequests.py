from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from leavebase.models import LeaveBase


class ListOfAllAppliedLeaves(View):
    template_name = 'leave/list_of_all_applied_leaves.html'

    @method_decorator(login_required)
    def get(self, request):
        get_leaves_for_user = LeaveBase.objects.filter(user_id=self.request.user.id)
        context = {
            "list_of_all_applied_leaves": get_leaves_for_user,
            "title": "All applied leaves",
            "page_id": "list_of_all_applied_leaves"
        }
        return render(request, self.template_name, context)
