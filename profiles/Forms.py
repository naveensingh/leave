from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Fieldset
from django import forms

from profiles.models import PersonalProfile


class PersonalProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=750)
    date_of_birth = forms.DateField(required=False, widget=forms.DateTimeInput(
                                    format='%d/%m/%Y',
                                    attrs={'class': 'al',
                                           'placeholder': 'dd/mm/yyyy',
                                           'data-date-format': 'dd/mm/yyyy'}))

    class Meta:
        model = PersonalProfile
        fields = ("date_of_birth", "profile_picture", "linkedin_url", "twitter_url", "bio")
