from django.shortcuts import render

# Create your views here.
from .models import Clothing, ClothingType, Outfit, Comment, Weather, User

def closet(request):
	#items in closet
	num_clothing = Clothing.objects.all().count()
	num_clothingtype = ClothingType.objects.all().count()
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
	user_name = User.objects.user_name
	
	return render(
		request,
		'friends.html',
		context={'num_user':num_user,'user_name':user_name},
	)
def profile(request):
	num_friends = User.objects.all().count()
	user_name = User.objects.user_name
	user_email = User.objects.email
	user_phone = User.objects.phone
	user_gender = User.objects.gender
	user_closet = User.objects.closet
	
	return render(
		request,
		'profile.html',
		context = {'user_name':user_name,'user_email':user_email,'user_phone':user_phone,'user_gender':user_gender,'user_closet':user_closet},
	)

	

