from datetime import date

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.generic import CreateView
from django.contrib.messages import error
from django.utils.translation import ugettext_lazy as _

from leavebase.models import LeaveBase


class ApplyForLeaveView(CreateView):
    template_name = 'leave/leave_application_form.html'

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
            self.reason = data.get("reason")[0]
            self.starting_from = data.get("starting_from")[0]
            self.ending_on = data.get("ending_on")[0]

            try:
                self.no_of_days = self.get_no_of_days(self.starting_from, self.ending_on).days
            except:
                self.no_of_days = 0
            leave = None
            try:
                leave = LeaveBase(user_id=self.request.user.id, name=self.request.user.first_name, reason=self.reason,
                                  starting_from=self.starting_from,
                                  ending_on=self.ending_on, no_of_days=self.no_of_days)
                leave.save()
            except:
                error(self.request, _("Failed to apply"))
            if leave:
                self.send_email_with_data()
                return HttpResponseRedirect("/leave/all")

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

    # Email to admin

    def send_email_with_data(self):
        template = get_template('leave/includes/request_leave_email_body.html')
        user_email = self.request.user.email
        context = Context({
            "domain": self.request.get_host(),
            "user_first_name": self.request.user.first_name,
            "reason": self.reason,
            "starting_from": self.starting_from,
            "ending_on": self.ending_on,
            "no_of_days": self.no_of_days
        })
        content = template.render(context)
        send_mail('Application for leave from office', content, '', [user_email], fail_silently=False)

        return True
