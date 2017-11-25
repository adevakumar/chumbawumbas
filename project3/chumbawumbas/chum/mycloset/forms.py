from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
# class UpdateProfileForm(forms.Form):
#     profile_picture = forms.CharField(max_length=200, help_text="Enter the url for your desired image")
#     description = forms.CharField(widget=forms.Textarea, max_length=1000, help_text="Enter a description for your profile")
#     gender = forms.CharField(max_length=1, help_text="Please Input F (Female), M (Male), or O (Other)")
#     phone = forms.CharField(max_length=10)
#     residence = forms.CharField(max_length=200, help_text="Enter your location of residence")


#     def clean_profile_picture(self):
#         data = self.cleaned_data['profile_picture']

#         # Remember to always return the cleaned data.
#         return data


#     def clean_description(self):
#         data = self.cleaned_data['description']

#         return data


#     def clean_gender(self):
#         data = self.cleaned_data['gender']

#         return data


#     def clean_phone(self):
#         data = self.cleaned_data['phone']

#         return data


#     def clean_residence(self):
#         data = self.cleaned_data['residence']

#         return data

