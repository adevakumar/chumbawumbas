from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class UpdateProfileForm(forms.Form):
    new_first_name = forms.CharField(help_text="Enter your preferred first name")
    new_last_name = forms.CharField(help_text="Enter your preferred last name")
    new_gender = forms.CharField(help_text="Enter a new gender. Input F (Female), M (Male), or O (Other)")
    new_residence = forms.CharField(help_text="Enter a new place of residence")
    new_phone = forms.CharField(help_text="Enter a new phone number")
    new_email = forms.EmailField(help_text="Enter a new valid email address")

    def clean_first_name(self):
        data = self.cleaned_data['new_first_name']

        # Remember to always return the cleaned data.
        return data

    def clean_last_name(self):
        data = self.cleaned_data['new_last_name']

        # Remember to always return the cleaned data.
        return data

    def clean_residence(self):
        data = self.cleaned_data['new_residence']

        # Remember to always return the cleaned data.
        return data

    def clean_gender(self):
        data = self.cleaned_data['new_gender']

        # Remember to always return the cleaned data.
        return data

    def clean_phone(self):
        data = self.cleaned_data['new_phone']

        # Remember to always return the cleaned data.
        return data

    def clean_email(self):
        data = self.cleaned_data['new_email']

        # Remember to always return the cleaned data.
        return data