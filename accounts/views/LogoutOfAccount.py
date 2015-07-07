from django.contrib.messages import info
from django.http import HttpResponseRedirect
from django.contrib.auth import (logout as auth_logout)
from django.utils.translation import ugettext_lazy as _


def logout(request):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)
    info(request, _("Successfully logged out"))
    return HttpResponseRedirect('/')
