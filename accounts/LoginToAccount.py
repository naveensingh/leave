from django.contrib.auth import authenticate, login
from django.contrib.messages import info, error
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from accounts.Forms.LoginForm import LoginForm


class LoginToAccount(View):
    template_name = "index.html"

    def setup(self):
        form = LoginForm(self.request.POST or None)
        self.form = form

    def get_context(self):
        self.setup()
        return {
            "title": "Login to your account",
            "form_class": "login-form"
        }

    def get(self, request, *args, **kwargs):
        self.setup()
        context = self.get_context()
        context["form"] = self.form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.setup()
        username = password = ''
        if self.form.is_valid():
            username = self.form.cleaned_data["username"]
            password = self.form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    info(request, _("Successfully logged in"))
                    return HttpResponseRedirect('/')
            else:
                error(request, _("You failed to login to your account"))
                return HttpResponseRedirect("/")
        else:
            error(request, _("You failed to login to your account"))
            return HttpResponseRedirect("/")
        context = self.get_context()
        return render_to_response(self.template_name, {'username': username}, context)

