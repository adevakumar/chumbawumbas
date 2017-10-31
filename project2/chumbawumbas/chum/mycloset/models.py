from django.db import models
#from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Clothing(models.Model):
    """
    Model representing clothing (but not a specific copy of a book).
    """
    clothing_name = models.CharField(max_length=200, help_text="Enter clothing name (e.g. Dark Wash Jeans)", default="")
    clothing_type = models.ForeignKey('ClothingType', on_delete=models.SET_NULL, null=True)
    weather = models.ForeignKey('Weather', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.clothing_name


class ClothingType(models.Model):
    """
    Model representing clothing classification (shirt, pants, etc)
    """
    type_name = models.CharField(max_length=200, help_text="Enter a clothing type (Shirt, Pants, etc.)")

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.name


class Outfit(models.Model):
    """
    Model representing clothing (but not a specific copy of a book).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")
    outfit_name = models.CharField(max_length=200, help_text="Enter outfit name")
    clothing = models.ManyToManyField(Clothing, help_text="Select all clothing for your outfit")
    date = models.DateField('Date', null=True, blank=True)

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.outfit_name

    def display_clothing(self):
        """
        Creates a string for clothing. This is required to display genre in Admin.
        """
        return ', '.join([ clothing.clothing_name for clothing in self.clothing.all()[:3] ])
    display_clothing.short_description = 'Clothing'


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    outfit = models.ForeignKey('Outfit', on_delete=models.CASCADE, null=True)
    date = models.DateField('Date', null=True, blank=True)


class Weather(models.Model):
    weather_type = models.CharField(max_length=20)
    date = models.DateField('Date', null=True, blank=True)
    

class User(models.Model):
    """
    Model representing an author.
    """
    user_name = models.CharField(max_length=200, help_text="Enter your name", default = '')
    phone = models.CharField('Phone Number',max_length=10)
    email = models.TextField('Email', max_length=1000, help_text="Enter your email address", default = '')
    gender = models.CharField('Gender', max_length=1, help_text="Please Input F (Female), M (Male), or O (Other)", default = '')
    closet = models.ManyToManyField('Clothing', help_text="Select clothing for closet")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.user_name)
