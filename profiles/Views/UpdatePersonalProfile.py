from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages import error
from django.utils.translation import ugettext_lazy as _
from profiles.forms import PersonalProfileForm
from profiles.models import PersonalProfile


class UpdatePersonalProfileView(CreateView):
    template_name = 'personalprofile/personal_profile_form.html'
    model = PersonalProfile
    form_class = PersonalProfileForm

    def setup(self):
        personal_profile, created = PersonalProfile.objects.get_or_create(user=self.request.user)
        self.profile_slug = personal_profile.profile_slug
        form = PersonalProfileForm(self.request.POST or None, self.request.FILES or None,
                                   instance=personal_profile or None)
        self.form = form

    def get_context(self):
        return {
            "title": "Edit Personal Profile",
            "body_class": "personal_profile"
        }

    def get(self, request, *args, **kwargs):
        self.setup()
        if request.user.is_authenticated():
            context = self.get_context()
            context['form'] = self.form
            context['title'] = "Edit Profile"
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
