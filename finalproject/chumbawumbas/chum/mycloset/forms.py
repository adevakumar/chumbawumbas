from django import forms

from .models import Weather, UserProfile, Clothing, ClothingType, Outfit, Comment

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


class AddClothingForm(forms.Form):
    new_clothing_name = forms.CharField(help_text="Enter the clothing name")
    new_clothing_type = forms.ModelChoiceField(queryset=ClothingType.objects.all())
    new_clothing_picture = forms.CharField(help_text="Enter a valid image URL")
    
    def clean_clothing_name(self):
        data = self.cleaned_data['new_clothing_name']
        return data

    def clean_clothing_type(self):
        data = self.cleaned_data['new_clothing_type']
        return data

    def clean_clothing_picture(self):
        data = self.cleaned_data['new_clothing_picture']
        return data


class AddOutfitForm(forms.Form):
    new_outfit_name = forms.CharField(help_text="Enter the outfit name")
    #Set dummy "none" query set until we can provide proper queryset (in __init__)
    new_clothing = forms.ModelMultipleChoiceField(queryset=Clothing.objects.none(), help_text="Ctrl-Click to add multiple items")

    #Required to get logged-in user to get their clothing
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AddOutfitForm, self).__init__(*args, **kwargs)
        qs = UserProfile.objects.get(user=user).closet
        self.fields['new_clothing'].queryset = qs
    
    def clean_outfit_name(self):
        data = self.cleaned_data['new_outfit_name']
        return data

    def clean_clothing(self):
        data = self.cleaned_data['new_clothing']
        return data


class DeleteClothingForm(forms.Form):
    class Meta:
        fields = []

class DeleteOutfitForm(forms.Form):
    class Meta:
        fields = []


class SaveSuggestionForm(forms.Form):
    new_outfit_name = forms.CharField(help_text="Enter a name for this new outfit")

    def clean_outfit_name(self):
        data = self.cleaned_data['new_outfit_name']

        # Remember to always return the cleaned data.
        return data