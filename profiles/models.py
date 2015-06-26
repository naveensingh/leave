import uuid

from autoslug import AutoSlugField
from django.db import models

from django.utils.translation import ugettext_lazy as _

from profiles import GENDER_CHOICES
from profiles.Helpers.AbstractUser import AbstractProfile
from settings.common import MEDIA_ROOT


def profile_picture_path(instance, filename):
    """
    Generate file name
    """
    return '/'.join([MEDIA_ROOT, 'users', instance.user.username, 'personal_profile', filename])


class PersonalProfile(AbstractProfile):
    profile_slug = AutoSlugField(unique=True, editable=False,
                                 populate_from=lambda instance: str(uuid.uuid4()),
                                 always_update=False, auto_created=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=GENDER_CHOICES)
    bio = models.CharField(blank=True, null=True, max_length=500, verbose_name=_("Short Bio"))
    job_title = models.CharField(blank=True, null=True, max_length=40)
    linkedin_url = models.URLField(blank=True, null=True, verbose_name=_("LinkedIn profile"))
    twitter_url = models.URLField(blank=True, null=True, verbose_name=_("Twitter profile"))
    profile_picture = models.ImageField(upload_to=profile_picture_path,
                                        max_length=255, null=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        """
        Return absolute url to the profile
        """
        return 'user_profile', (), {'profile_slug': self.profile_slug}

