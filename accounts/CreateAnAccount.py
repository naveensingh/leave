from django.contrib.auth.models import User
from django.contrib.messages import info, error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from accounts.Forms.SignUpForm import SignupForm
from django.utils.translation import ugettext_lazy as _

class CreateAnAccount(CreateView):
    template_name = "accounts/accountsform.html"
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
            self.form.save()
            info(request, _("Successfully signed up"))
            return HttpResponseRedirect("/")
        else:
            error(request, _("You failed to signed up"))
            return HttpResponseRedirect("/")
