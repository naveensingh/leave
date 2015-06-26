from django.shortcuts import render
from django.views.generic import View


class LandingView(View):
    template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated():
            context = {
                "title": "You are logged in",
            }
        else:
            context = {
                "title": "Login to your account",
            }
        return render(request, self.template_name, context)
