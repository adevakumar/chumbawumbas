from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class UpdateProfileForm(forms.Form):
    new_residence = forms.CharField(help_text="Enter a new place of residence")

    def clean_residence(self):
        data = self.cleaned_data['new_residence']

        # Remember to always return the cleaned data.
        return data