from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Fieldset
from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.CharField(label=_("Email"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(render_value=False))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
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
                Submit('submit', 'Login to your account',
                       css_class='btn btn-primary text-center'),

            ),
        )
