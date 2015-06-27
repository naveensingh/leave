from django.shortcuts import render
from django.views.generic import View
from profiles.models import PersonalProfile


class PersonalProfileView(View):
    template_name = 'personal_profile.html'

    def get(self, request, profile_slug):
        profile = PersonalProfile.objects.get(profile_slug=profile_slug)

        context = {
            "profile": profile,
            "title": "My Profile",
        }
        return render(request, self.template_name, context)
