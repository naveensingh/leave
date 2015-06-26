from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.layout import Fieldset
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignupForm(forms.ModelForm):
    
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ("email", )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self._signup = self.instance.id is None
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.label_class = 'control-label'
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('email', autocomplete='off'),
                Field('password', autocomplete='off'),
            ),
            FormActions(
                Submit('submit', 'Create an account',
                       css_class='btn btn-primary text-center'),

            ),
        )
