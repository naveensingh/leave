from django.shortcuts import render
from django.views.generic import View


class LandingView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {
            "title": "Latest Articles",
        }
        return render(request, self.template_name, context)