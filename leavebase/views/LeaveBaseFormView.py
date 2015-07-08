from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages import error
from leavebase.models import LeaveBase


class ApplyForLeaveView(CreateView):
    template_name = 'leave/form.html'
    # form_class = LeaveBaseForm
    #
    # def setup(self):
    #     # get_leave_slug = self.kwargs.get("leave_slug")
    #     a = LeaveBase.objects.get_or_create(user=self.request.user)
    #     form = self.form_class(self.request.POST or None, self.request.FILES or None,
    #                            instance=a or None)
    #     self.form = form

    def get_context(self):
        return {
            "title": "Apply for leave",
            "body_class": "leave_body"
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
            reason = data.get("reason")[0]
            starting_from = data.get("starting_from")[0]
            ending_on = data.get("ending_on")[0]
            leave = LeaveBase(user_id=self.request.user.id, name=self.request.user.first_name, reason=reason,
                              starting_from=starting_from,
                              ending_on=ending_on)
            leave.save()
            return HttpResponseRedirect("/leave/all")
        context = self.get_context()
        return render(request, self.template_name, context)
