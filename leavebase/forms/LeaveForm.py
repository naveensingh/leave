# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Field
# from django import forms
#
#
# class LeaveBaseForm(forms.Form):
#     reason = forms.CharField(max_length=100)
#     starting_from = forms.CharField(max_length=100)
#     ending_on = forms.CharField()
#
#     def __init__(self, *args, **kwargs):
#         super(LeaveBaseForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.form_class = 'form-horizontal well'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-8'
#
#         self.helper.layout = Layout(
#             Div(
#                 Field('reason'),
#                 Field('starting_from'),
#                 Field('ending_on'),
#                 Field('no_of_days'),
#             ),
#         )
