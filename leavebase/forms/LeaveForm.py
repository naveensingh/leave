# import datetime
#
# from crispy_forms.bootstrap import AppendedText, Accordion, AccordionGroup
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Field
# from django import forms
#
# from khapps.trial import CONFIDENTIALITY_TYPE, AUTHOR_POSITION, STAT_ANALYSIS_METHOD
# from khapps.khutils.django.FormUtils import FormUtils
#
#
# class ProtocolForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     trial_code = forms.CharField(max_length=100)
#     harvest_year = forms.IntegerField()
#
#     def __init__(self, *args, **kwargs):
#         super(ProtocolForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.form_class = 'form-horizontal well'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-8'
#
#         self.helper.layout = Layout(
#             Div(
#                 Field('title'),
#                 Field('trial_code'),
#                 Field('harvest_year'),
#                 css_class='col-md-6'
#             ),
#         )
