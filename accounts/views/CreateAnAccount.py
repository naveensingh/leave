from autoslug.utils import slugify
from django.contrib.auth.models import User
from django.contrib.messages import info, error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms.SignUpForm import SignupForm
from django.utils.translation import ugettext_lazy as _

class CreateAnAccount(CreateView):
    template_name = "accounts/signup.html"
    model = User

    def setup(self):
        self.form = SignupForm(self.request.POST or None)

    def get_context(self):
        return {
            "page_id": "create_an_account",
            "title": "Create an account",
        }

    def get(self, request, *args, **kwargs):
        self.setup()
        context = self.get_context()
        context['form'] = self.form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.setup()
        if request.method == "POST" and self.form.is_valid():
            email = self.form.cleaned_data["email"]
            if self.check_email(email):
                username_from_email = self.build_username(email)
                self.form.instance.username = username_from_email
                self.form.save()
                info(request, _("Successfully signed up"))
                return HttpResponseRedirect("/")
            else:
                error(self.request, _("You failed to signed up"))

        context = self.get_context()
        context['form'] = self.form
        return render(request, self.template_name, context)

    def build_username(self, email):
        username = slugify(email).lower()
        if len(username) > 30:
            username = username[:30]
        lookup = {"username__iexact": username}
        try:
            User.objects.exclude(id=self.form.instance.id).get(**lookup)
        except User.DoesNotExist:
            return username

    def check_email(self, email):
        qs = User.objects.exclude(id=self.form.instance.id).filter(email=email)
        if len(qs) == 0:
            return email
