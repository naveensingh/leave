from django.shortcuts import render
from django.views.generic import View
from leavebase.models import LeaveBase

from profiles.Views.CalculateNoOfLeaves import get_no_of_leaves_by_user
from profiles.models import PersonalProfile


class PersonalProfileView(View):
    template_name = 'personal_profile.html'

    def get(self, request, profile_slug):
        profile = PersonalProfile.objects.get(profile_slug=profile_slug)

        context = {
            "profile": profile,
            "total_leaves_by_user": self.get_no_of_leaves_by_user(),
            "user_overdue": self.intelligent_leave_calculation,
            "title": "My Profile",
        }
        return render(request, self.template_name, context)

    def get_no_of_leaves_by_user(self):

        get_leaves_of_user = LeaveBase.objects.filter(user_id=self.request.user.id)
        get_no_of_days = get_leaves_of_user.values_list("no_of_days")
        total_no_of_days = sum(get_no_of_days)
        return total_no_of_days

    def intelligent_leave_calculation(self):
        total_leaves_by_user = 28 - get_no_of_leaves_by_user(self.request.user.id)
        if total_leaves_by_user < 0:
            user_overdue = total_leaves_by_user
        else:
            user_overdue = None

        return user_overdue
