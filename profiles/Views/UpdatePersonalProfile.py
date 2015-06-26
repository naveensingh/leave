from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages import error
from django.utils.translation import ugettext_lazy as _

from profiles.forms import PersonalProfileForm
from profiles.models import PersonalProfile


class UpdatePersonalProfileView(CreateView):
    template_name = 'accounts/accountsform.html'
    model = PersonalProfile
    form_class = PersonalProfileForm

    def setup(self):
        form = PersonalProfileForm(self.request.POST or None, self.request.FILES or None)
        self.form = form

    def get_context(self):
        return {
            "title": "Edit Personal Profile",
            "specific_class": "specific_class"
        }

    def get(self, request, *args, **kwargs):
        self.setup()
        if request.user.is_authenticated():
            print "hello"
            print request.user.id
            context = self.get_context()
            context['form'] = self.form
            context['title'] = "Edit Personal Profile"
            return render(request, self.template_name, context)
        else:
            error(request, "Please log in to your account")
            return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        self.setup()
        if request.method == "POST":
            if self.form.is_valid():
                self.form.instance.user_id = request.user.id
                self.form.save()
                return HttpResponseRedirect('/')
            else:
                error(self.request, _("Couldn't update your profile"))

        context = self.get_context()
        context['form'] = self.form
        context['title'] = "Edit Personal Profile"
        return render(request, self.template_name, context)
