from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.messages import info, error
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from accounts.forms.LoginForm import LoginForm
from autoslug.utils import slugify


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

            build_username = self.build_username(username)
            user = authenticate(username=build_username, password=password)
            if self.check_email(username):
                self.form.instance.username = build_username
                self.form.instance.email = username
                self.form.save()
                login(request, user)
                info(request, _("Successfully signed up"))
                return HttpResponseRedirect("/")
            else:
                login(request, user)
                info(request, _("Successfully logged in"))
                return HttpResponseRedirect('/')

        else:
            error(request, _("You failed to login to your account"))
            return HttpResponseRedirect("/")

    def build_username(self, email):
        username = slugify(email).lower()
        if len(username) > 30:
            username = username[:30]
        lookup = {"username__iexact": username}
        try:
            User.objects.exclude(id=self.form.instance.id).get(**lookup)
        except User.DoesNotExist:
            return username

    def check_email(self, username):
        qs = User.objects.exclude(id=self.form.instance.id).filter(email=username)
        if len(qs) == 0:
            return username
