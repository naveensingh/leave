from django.contrib.auth.models import User
from django.db import models


class AbstractProfile(models.Model):
    user = models.OneToOneField(User, unique=True, editable=False)

    class Meta:
        abstract = True
