from django.db import models
#from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

from django.contrib.auth.models import User

class Clothing(models.Model):
    """
    Model representing clothing.
    """
    clothing_name = models.CharField(max_length=200, help_text="Enter clothing name (e.g. Dark Wash Jeans)", default="")
    clothing_type = models.ForeignKey('ClothingType', on_delete=models.SET_NULL, null=True)
    clothing_picture = models.CharField(max_length=200, help_text="Enter the url for your desired image", null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.clothing_name


class ClothingType(models.Model):
    """
    Model representing clothing classification.
    """
    type_name = models.CharField(max_length=200, help_text="Enter a clothing classification")

    def __str__(self):
        """
        String for representing the ClothingType object.
        """
        return self.type_name


class Outfit(models.Model):
    """
    Model representing an Outfit.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    IS_FAVORITE = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    favorite = models.CharField(max_length=1, choices=IS_FAVORITE, default='N')
    outfit_name = models.CharField(max_length=200, help_text="Enter outfit name")
    clothing = models.ManyToManyField(Clothing, help_text="Select all clothing for your outfit")
    date = models.DateField('Date', null=True, blank=True)

    def __str__(self):
        """
        String for representing the Outfit object.
        """
        return self.outfit_name

    def display_clothing(self):
        """
        Creates a string for outfit.
        """
        return ', '.join([ clothing.clothing_name for clothing in self.clothing.all()[:3] ])
    display_clothing.short_description = 'Clothing'


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)
    outfit = models.ForeignKey('Outfit', on_delete=models.CASCADE, null=True)
    date = models.DateField('Date', null=True, blank=True)

class WeatherType(models.Model):
    """
    Model representing weather classification (sunny, rainy, etc)
    """
    type_name = models.CharField(max_length=200, help_text="Enter a clothing type (Shirt, Pants, etc.)")
    clothing_types = models.ManyToManyField('ClothingType', help_text="Select clothing types to be simultaneously worn in this weather")

    def display_clothing_types(self):
        """
        Creates a string for user.username. This is required to display username in Admin.
        """
        return ', '.join([ clothing_types.type_name for clothing_types in self.clothing_types.all()[:3] ])
    display_clothing_types.short_description = 'Clothing Types'

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.type_name


class Weather(models.Model):
    weather_type = models.ForeignKey('WeatherType', on_delete=models.SET_NULL, null=True)
    date = models.DateField('Date', null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.weather_type)


class WeatherSuggestion(models.Model):
    suggestion_name = models.CharField(max_length=100, default="Not Used", help_text="Enter the name for this weather suggestion")
    clothing_types = models.ManyToManyField(ClothingType, help_text="Select the clothing types to be worn for this type of weather")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.suggestion_name)


from django.db.models.signals import post_save
from django.dispatch import receiver    

class UserProfile(models.Model):
    """
    Model representing an author.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.CharField(max_length=200, help_text="Enter the url for your desired image", null=True)
    description = models.TextField(max_length=1000, help_text="Enter a description for your profile", null=True)
    phone = models.CharField('Phone Number',max_length=10)
    gender = models.CharField('Gender', max_length=1, help_text="Please Input F (Female), M (Male), or O (Other)", default = '')
    residence = models.CharField('Residence', max_length=200, help_text="Enter your location of residence", default = '')
    closet = models.ManyToManyField('Clothing', help_text="Select clothing for closet")
    friends = models.ManyToManyField('UserProfile', help_text="Select friends for this user")
    maximum_cold_temperature = models.IntegerField(default="5", help_text="Please enter the maximum temperature (Celsius) that you would consider cold. Temperatures above this are cool, then warm, then hot.")
    maximum_cool_temperature = models.IntegerField(default="16", help_text="Please enter the maximum temperature (Celsius) that you would consider cool. Temperatures above this are warm, then hot.")
    maximum_warm_temperature = models.IntegerField(default="27", help_text="Please enter the maximum temperature (Celsius) that you would consider warm. Temperatures above this are hot.")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def display_user_name(self):
        """
        Creates a string for user.username. This is required to display username in Admin.
        """
        return self.user.username

    def display_email(self):
        """
        Creates a string for user.username. This is required to display username in Admin.
        """
        return self.user.email

    def display_clothing(self):
        """
        Creates a string for user.username. This is required to display username in Admin.
        """
        return ', '.join([ closet.clothing_name for closet in self.closet.all()[:3] ])
    display_clothing.short_description = 'Closet'

    def display_friends(self):
        """
        Creates a string for user.username. This is required to display username in Admin.
        """
        return ', '.join([ friends.user.username for friends in self.friends.all()[:3] ])
    display_friends.short_description = 'Friends'

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.user.username)
