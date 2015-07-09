from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages import error, info
from django.utils.translation import ugettext_lazy as _

from leavebase.models import LeaveBase


class ApplyForLeaveView(CreateView):
    template_name = 'leave/leave_application_form.html'
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

            try:
                no_of_days = self.get_no_of_days(starting_from, ending_on).days
            except:
                no_of_days = 0
            try:
                leave = LeaveBase(user_id=self.request.user.id, name=self.request.user.first_name, reason=reason,
                                  starting_from=starting_from,
                                  ending_on=ending_on, no_of_days=no_of_days)
                leave.save()
                info(self.request, _("Applied"))
                return HttpResponseRedirect("/leave/all")
            except:
                error(self.request, _("Failed to apply"))

        context = self.get_context()
        return render(request, self.template_name, context)

    def get_no_of_days(self, starting_from, ending_on):
        get_starting_date = self.make_date_list(str(starting_from))
        get_ending_date = self.make_date_list(str(ending_on))

        get_days = get_ending_date - get_starting_date

        return get_days

    def make_date_list(self, get_date):
        replace_starting_from = str(get_date).replace("/", ",")
        get_starting_date_list = replace_starting_from.rstrip(",").split(',')
        get_starting_date = date(int(get_starting_date_list[2]), int(get_starting_date_list[1]),
                                 int(get_starting_date_list[0]))

        return get_starting_date
