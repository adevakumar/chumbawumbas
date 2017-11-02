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
	num_clothing = Clothing.objects.all().count()
	num_clothingtype = ClothingType.objects.all().count()
	clothing_type = Clothing.objects.get(clothing_type)
	clothing_picture = Clothing.objects.get(clothing_picture)
	num_outfits = Outfit.objects.all().count()
	num_comments = Comment.objects.all().count()
	num_weather = Weather.objects.all().count()
	num_user = User.objects.all().count()

	return render(
		request,
		'closet.html',
		context={'num_clothing':num_clothing,'num_clothingtype':num_clothingtype,'num_outfits':num_outfits,'num_weather':num_weather,'num_user':num_user},
	)

def friends(request):
	num_user = User.objects.all().count()
	user_name = User.objects.get(user_name)

	return render(
		request,
		'friends.html',
		context={'num_user':num_user,'user_name':user_name},
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
        date = Weather.objects.get(date)
        wtype = Weather.objects.get(wtype='Cloudy')

	return render(
		request,
		'weather.html',
		context = {'date':date,'wtype':wtype},
	)


def about(request):

	return render(
		request,
		'fifth.html',
		context = {},
	)
