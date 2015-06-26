from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Fieldset
from django import forms

from profiles.models import PersonalProfile


class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalProfile
        fields = ("date_of_birth", "gender", "job_title", "profile_picture", "linkedin_url", "twitter_url", "bio")
        widgets = {
            'date_of_birth': forms.DateInput(format='%m/%d/%Y',
                                             attrs={
                                                 'placeholder': 'mm/dd/yyyy',
                                                 'data-date-format': 'mm/dd/yyyy'
                                             }),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.label_class = 'control-label'
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('date_of_birth', '<i class="icon-calendar bigger-110"></i>', css_class='date-picker'),
                Field('gender'),
                Field('job_title'),
                Field('profile_picture'),
                Field('linkedin_url'),
                Field('twitter_url'),
                Field('bio'),
            ),
            FormActions(
                Submit('submit', 'Save Profile',
                       css_class='btn btn-primary text-center'),

            ),
        )
