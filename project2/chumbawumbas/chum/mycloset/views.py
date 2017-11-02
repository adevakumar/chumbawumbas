from django.shortcuts import render

# Create your views here.
from .models import Clothing, ClothingType, Outfit, Comment, Weather, User

def index(request):
	"""
	View function for the home page of our site.
	"""
	# Put desired data fields here to allow for referencing in html for home page (index)
	# Example: num_books=Book.objects.all().count()
	# DONT FORGET TO ALSO POPULATE THE CONTEXT ARRAY IN THE THE RETURN STATEMENT BELOW


	return render(
		request,
		'index.html',
		context={},
	)

def closet(request):
#items in closet
	closet_clothing = Outfit.objects.all()
	types = ClothingType.objects.get(type_name = "Skirt")
	specific_outfit = Outfit.objects.get(outfit_name = "Formal")
	specific_weather = Weather.objects.get(weather_type = "Cloudy")

	return render(
		request,
		'closet.html',
		context={'closet_clothing':closet_clothing, 'types':types, 'specific_outfit':specific_outfit, 'specific_weather':specific_weather}
)

def friends(request):
	user1 = User.objects.get(user_name = 'Tim Richards')
	user2 = User.objects.get(user_name = 'Bob')
	user3 = User.objects.get(user_name = 'Michelle')
	num_user = User.objects.all().count()

	return render(
		request,
		'friends.html',
		context={'num_user':num_user,'user_one':user1, 'user_two':user2, 'user_three':user3},
	)

def profile(request):
	user = User.objects.get(user_name='Seth')
	previous_outfits = Outfit.objects.filter(user__user_name='Seth')[:3]
	favorite_outfits = Outfit.objects.filter(user__user_name='Seth').filter(favorite='Y')


	return render(
		request,
		'profile.html',
		context = {'user':user, 'previous_outfits':previous_outfits, 'favorite_outfits':favorite_outfits},
        )


def weather(request):
        date = Weather.objects.get(date='2017-11-02')
        date2 = Weather.objects.get(date='2017-11-03')
        date3 = Weather.objects.get(date='2017-11-04')
        date4 = Weather.objects.get(date='2017-11-05')
        weather_type = Weather.objects.get(weather_type='Cloudy')

        return render(
		request,
		'weather.html',
		context = {'date':date,'date2':date2,'date3':date3,'date4':date4,'weather_type':weather_type},
	)


def about(request):

	return render(
		request,
		'fifth.html',
		context = {},
	)
