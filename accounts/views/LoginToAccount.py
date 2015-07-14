from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.messages import info, error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from autoslug.utils import slugify

from accounts.forms.LoginForm import LoginForm


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
        email = password = ''
        if self.form.is_valid():
            email = self.form.cleaned_data["email"]
            password = self.form.cleaned_data["password"]
            if self.validate_email(email):
                self.new_username = self.build_username(email)
                if self.check_email(email):
                    self.login_user(password)
                    return HttpResponseRedirect('/')
                else:
                    self.create_new_user(email, password)
                    self.login_user(password)
                    info(request, _("Successfully signed up and logged in"))
                    return HttpResponseRedirect("/")
            error(request, _("You failed to login to your account"))
            return HttpResponseRedirect("/")
        else:
            error(request, _("You failed to login to your account"))
            return HttpResponseRedirect("/")

    def build_username(self, email):
        username_from_email = slugify(email).lower()
        if len(username_from_email) > 30:
            username_from_email = username_from_email[:30]
        return username_from_email

    def check_email(self, email):
        user = User.objects.filter(email=email)
        if len(user) == 0:
            return None
        else:
            return user

    def create_new_user(self, email, password):
        new_user = User()
        build_username = self.build_username(email)
        new_user.username = build_username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        return new_user

    def login_user(self, password):
        user = authenticate(username=self.new_username, password=password)
        if user:
            info(self.request, _("Successfully logged in"))
            return login(self.request, user)
        else:
            info(self.request, _("Password wrong in"))
            return HttpResponseRedirect('/')

    def validate_email(self, email):
        if "@kisanhub.com" in email:
            count = email.count("@")
            if count > 1:
                return False
            else:
                return True
        else:
            return False