from django.db import models
#from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Clothing(models.Model):
    """
    Model representing clothing (but not a specific copy of a book).
    """
    clothing_type = models.CharField(max_length=200)
    #summary = models.CharField(max_length=100, help_text="Enter Clothing Type")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")

    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.clothing_type

class Outfit(models.Model):
    """
    Model representing clothing (but not a specific copy of a book).
    """
    #outfit_type = models.CharField(max_length=200)
    #summary = models.CharField(max_length=100, help_text="Enter Clothing Type")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular clothing across whole closet")
    OutfitName = models.CharField(max_length=200, help_text="Enter outfit name")
    clothing = models.ManyToManyField(Clothing, help_text="Select all clothing for your outfit")
    date = models.DateField('Date', null=True, blank=True)
    userComment = models.ForeignKey('Comments', on_delete=models.SET_NULL, null=True)
	
    def __str__(self):
        """
        String for representing the Clothing object.
        """
        return self.OutfitName
        
class Comments(models.Model):
	singleComment = models.TextField(max_length=2000)

class User(models.Model):
    """
    Model representing an author.
    """
    user_name = models.CharField(max_length=200, help_text="Enter your name", default = '')
    phone = models.CharField('phone number',max_length=10)
    contactInfo = models.TextField('Contact Info', max_length=1000, help_text="Enter your email address", default = '')
    gender = models.CharField('Gender', max_length=1, help_text="Please Input F (Female), M (Male), or O (Other)", default = '')
    closet = models.ManyToManyField('Clothing', help_text="Select clothing for closet")
    #friends = models.ManyToManyField(self, help_text="Add your friends to the list")
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.user_name)
