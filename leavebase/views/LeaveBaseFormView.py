from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages import error
from leavebase.models import LeaveBase


class ApplyForLeaveView(CreateView):
    template_name = 'leave/form.html'

    # def setup(self):
    #     personal_profile, created = PersonalProfile.objects.get_or_create(user=self.request.user)
    #     self.profile_slug = personal_profile.profile_slug
    #     form = PersonalProfileForm(self.request.POST or None, self.request.FILES or None,
    #                                instance=personal_profile or None)
    #     self.form = form

    def get_context(self):
        return {
            "title": "Apply for leave",
            "specific_class": "specific_class"
        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            context = self.get_context()
            return render(request, self.template_name, context)
        else:
            error(request, "Please log in to your account")
            return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            alldata = dict(request.POST.iterlists())
            data = dict(alldata)
            name = data.get("name")[0]
            reason = data.get("reason")[0]
            starting_from = data.get("starting_from")[0]
            ending_on = data.get("ending_on")[0]
            no_of_days = data.get("no_of_days")[0]
            leave = LeaveBase(user_id=self.request.user.id, name=name, reason=reason, starting_from=starting_from,
                              ending_on=ending_on)
            leave.save()
            return HttpResponseRedirect("/leave/all")
        context = self.get_context()
        return render(request, self.template_name, context)
