from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import datetime
import random
import urllib.request
import json
import operator

# Create your views here.
from .models import Clothing, ClothingType, Outfit, Comment, Weather, WeatherSuggestion, UserProfile

def index(request):
	"""
	View function for the home page of our site.
	"""

	return render(
		request,
		'index.html',
		context={},
	)

@login_required
def closet(request):
	user_profile = UserProfile.objects.get(user=request.user)

	# API Weather Data retrieval
	api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b4577d3c39fbd5525c092580382decc6&q='
	city = user_profile.residence
	api_url = (api_address + city)
	with urllib.request.urlopen(api_url) as response:
		json_weather_data = json.load(response)
	weather_temperature = json_weather_data['main']['temp'] - 273.15

	#Getting todays weather from our database
	todays_date = datetime.date.today()
	#weather_today = Weather.objects.get(date__year=todays_date.year, date__month=todays_date.month, date__day=todays_date.day)

	if weather_temperature <= user_profile.maximum_cold_temperature:
		suggestion_type = WeatherSuggestion.objects.get(suggestion_name="Cold Suggestion")
	elif weather_temperature <= user_profile.maximum_cool_temperature:
		suggestion_type = WeatherSuggestion.objects.get(suggestion_name="Cool Suggestion")
	elif weather_temperature <= user_profile.maximum_warm_temperature:
		suggestion_type = WeatherSuggestion.objects.get(suggestion_name="Warm Suggestion")
	else:
		suggestion_type = WeatherSuggestion.objects.get(suggestion_name="Hot Suggestion")

	#Make outfit but don't save it to the database yet!
	suggested_outfit = Outfit(user=request.user, outfit_name="Current Suggestion", date=todays_date)
	if Outfit.objects.filter(outfit_name="Current Suggestion", user=request.user).exists():
		# If there is already a suggestion, need to delete it first
		Outfit.objects.get(outfit_name="Current Suggestion", user=request.user).delete()

	for current_clothing_type in suggestion_type.clothing_types.all():
		available_clothing_of_current_type = user_profile.closet.filter(clothing_type=current_clothing_type)
		if len(available_clothing_of_current_type) == 0:
			clothing_choice = 'None'
		elif len(available_clothing_of_current_type) == 1:
			clothing_choice = available_clothing_of_current_type[0]
			suggested_outfit.clothing.add(clothing_choice)
		else:
			clothing_choice = available_clothing_of_current_type[random.randint(0,len(available_clothing_of_current_type)-1)]
			suggested_outfit.clothing.add(clothing_choice)

	# Save the suggestion to the database (until a new one is made)
	suggested_outfit.save()
	#End

	#Get outfits and clothing for current logged-in user
	closet_outfits = Outfit.objects.filter(user=request.user)
	closet_clothing = user_profile.closet

	return render(
		request,
		'closet.html',
		context={'user_profile': user_profile, 'suggested_outfit': suggested_outfit,'closet_outfits':closet_outfits, 'closet_clothing': closet_clothing, 'json_weather_data': json_weather_data},
)

@login_required
def friends(request):
	user_profile = UserProfile.objects.get(user=request.user)
	num_user = UserProfile.objects.all().count()

	return render(
		request,
		'friends.html',
		context={'num_user':num_user,'user_profile':user_profile},
	)


@login_required
def profile(request):
	user_profile = UserProfile.objects.get(user=request.user)

	previous_outfits = Outfit.objects.filter(user=request.user).order_by('-date')[:5]
	favorite_outfits = Outfit.objects.filter(user=request.user).filter(favorite='Y')

	return render(
		request,
		'profile.html',
		context = {'user_profile':user_profile, 'previous_outfits':previous_outfits, 'favorite_outfits':favorite_outfits},
        )


@login_required
def weather(request):
	user_profile = UserProfile.objects.get(user=request.user)
	city = user_profile.residence

	# API Weather Data retrieval
	api_weather_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b4577d3c39fbd5525c092580382decc6&q='
	api_weather_url = (api_weather_address + city)
	with urllib.request.urlopen(api_weather_url) as response:
		json_weather_data = json.load(response)

	# API Forecast Data Retrieval
	api_forecast_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=b4577d3c39fbd5525c092580382decc6&q='
	api_forecast_url = (api_forecast_address + city)
	with urllib.request.urlopen(api_forecast_url) as response:
		json_forecast_data = json.load(response)

	todays_date = datetime.date.today()
	# date = Weather.objects.get(date__year=todays_date.year, date__month=todays_date.month, date__day=todays_date.day)
	# tomorrows_date = todays_date + datetime.timedelta(days=1)
	# date2 = Weather.objects.get(date__year=tomorrows_date.year, date__month=tomorrows_date.month, date__day=tomorrows_date.day)
	# two_days_from_now = tomorrows_date + datetime.timedelta(days=1)
	# date3 = Weather.objects.get(date__year=two_days_from_now.year, date__month=two_days_from_now.month, date__day=two_days_from_now.day)
	# three_days_from_now = two_days_from_now + datetime.timedelta(days=1)
	# date4 = Weather.objects.get(date__year=three_days_from_now.year, date__month=three_days_from_now.month, date__day=three_days_from_now.day)
	# weather_type = Weather.objects.filter(weather_type__type_name='Cloudy')

	return render(
		request,
		'weather.html',
		context = {'user_profile':user_profile, 'json_weather_data': json_weather_data, 'json_forecast_data': json_forecast_data},
	)


def about(request):

	return render(
		request,
		'fifth.html',
		context = {},
	)


#from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import UpdateProfileForm
from .forms import AddClothingForm
from .forms import AddOutfitForm
from .forms import DeleteClothingForm
from .forms import DeleteOutfitForm
from .forms import SaveSuggestionForm

#@permission_required('catalog.can_mark_returned')
def update_profile(request, pk):
    """
    View function for updating a user profile
    """
    user_profile=get_object_or_404(UserProfile, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UpdateProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_profile.user.first_name = form.cleaned_data['new_first_name']
            user_profile.user.last_name = form.cleaned_data['new_last_name']
            user_profile.gender = form.cleaned_data['new_gender']
            user_profile.residence = form.cleaned_data['new_residence']
            user_profile.phone = form.cleaned_data['new_phone']
            user_profile.user.email = form.cleaned_data['new_email']
            user_profile.user.save()
            user_profile.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profile') )

    # If this is a GET (or any other method) create the default form.
    else:
      proposed_first_name = user_profile.user.first_name
      proposed_last_name = user_profile.user.last_name
      proposed_residence = user_profile.residence
      proposed_gender = user_profile.gender
      proposed_phone = user_profile.phone
      proposed_email = user_profile.user.email
      form = UpdateProfileForm(initial={'new_first_name': proposed_first_name, 'new_last_name': proposed_last_name,'new_residence': proposed_residence, 'new_gender': proposed_gender, 'new_phone': proposed_phone, 'new_email': proposed_email,})

    return render(request, 'mycloset/update_profile.html', {'form': form, 'user_profile':user_profile})


def add_clothing(request, pk):
	"""
	View function for adding clothing to your closet
	"""
	user_profile=get_object_or_404(UserProfile, pk = pk)

	if request.method == 'POST':

		form = AddClothingForm(request.POST)

		if form.is_valid():
			clothing = Clothing.objects.create(clothing_name=form.cleaned_data['new_clothing_name'], clothing_type=form.cleaned_data['new_clothing_type'], clothing_picture=form.cleaned_data['new_clothing_picture'])
			user_profile.closet.add(clothing)
			user_profile.save()

			return HttpResponseRedirect(reverse('closet'))

	else:
		form = AddClothingForm()

	return render(request, 'mycloset/add_clothing.html', {'form': form, 'user_profile': user_profile})


def add_outfit(request, pk):
	"""
	View function for adding an outfit to your closet
	"""
	user_profile=get_object_or_404(UserProfile, pk = pk)

	if request.method == 'POST':

		form = AddOutfitForm(request.POST, user=request.user)

		if form.is_valid():
			outfit = Outfit.objects.create(user=request.user, outfit_name=form.cleaned_data['new_outfit_name'], clothing=form.cleaned_data['new_clothing'], date=datetime.date.today())

			return HttpResponseRedirect(reverse('closet'))

	else:
		form = AddOutfitForm(user=request.user)

	return render(request, 'mycloset/add_outfit.html', {'form': form, 'user_profile': user_profile})


def search_users(request):
	"""
	View function for searching for users using the search bar
	"""
	input_username = request.GET.get('input_text')
	searched_user = UserProfile.objects.get(user__username=input_username)
	previous_outfits = Outfit.objects.filter(user__username=input_username)[:3]
	favorite_outfits = Outfit.objects.filter(user__username=input_username).filter(favorite='Y')
	#print(searched_user.user.first_name)

	return render(
		request, 
		'mycloset/searched_profile.html', 
		context= {'searched_user': searched_user, 'previous_outfits': previous_outfits,'favorite_outfits': favorite_outfits},
	)


def delete_clothing(request, pk):
	"""
	View function for adding an outfit to your closet
	"""
	clothing_to_delete=get_object_or_404(Clothing, pk = pk)

	if request.method == 'POST':

		form = DeleteClothingForm(request.POST)

		if form.is_valid():
			Clothing.delete(clothing_to_delete)

			return HttpResponseRedirect(reverse('closet'))

	else:
		form = DeleteClothingForm()

	return render(request, 'mycloset/delete_clothing.html', {'form': form, 'clothing_to_delete': clothing_to_delete})


def delete_outfit(request, pk):
	"""
	View function for adding an outfit to your closet
	"""
	outfit_to_delete=get_object_or_404(Outfit, pk = pk)

	if request.method == 'POST':

		form = DeleteOutfitForm(request.POST)

		if form.is_valid():
			Outfit.delete(outfit_to_delete)

			return HttpResponseRedirect(reverse('closet'))

	else:
		form = DeleteOutfitForm()

	return render(request, 'mycloset/delete_outfit.html', {'form': form, 'outfit_to_delete': outfit_to_delete})


def save_suggestion(request, pk):
    """
    View function for updating a user profile
    """
    suggestion=get_object_or_404(Outfit, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SaveSuggestionForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            suggestion.outfit_name = form.cleaned_data['new_outfit_name']
            suggestion.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('closet') )

    # If this is a GET (or any other method) create the default form.
    else:
      form = SaveSuggestionForm(initial={})

    return render(request, 'mycloset/save_suggestion.html', {'form': form, 'suggestion':suggestion})


def set_favorite(request):

	if request.method == 'POST':
		outfit_id = request.POST.get('outfit_id')

		outfit = get_object_or_404(Outfit, pk = outfit_id)

		if outfit.favorite == 'Y':
			outfit.favorite = 'N'
		else:
			outfit.favorite = 'Y'
		outfit.save()

		return HttpResponseRedirect(reverse('closet'))
	else:
		# Do nothing then go back to closet
		return render(request, 'closet.html', context={},)


def view_outfit(request, pk):

	current_outfit=get_object_or_404(Outfit, pk = pk)
	comments=Comment.objects.filter(outfit__id=current_outfit.id).order_by('date')

	return render(request, 'mycloset/view_outfit.html', context={'current_outfit':current_outfit, 'comments':comments})


def submit_comment(request, user_id, outfit_id):

	user_profile=UserProfile.objects.get(user__id=user_id)
	current_outfit=get_object_or_404(Outfit, pk = outfit_id)

	Comment.objects.create(user_profile=user_profile, outfit=current_outfit, text=request.POST.get('comment_text'), date=datetime.date.today())

	comments=Comment.objects.filter(outfit__id=current_outfit.id).order_by('date')

	return render(
		request, 
		'mycloset/view_outfit.html', 
		context={'current_outfit':current_outfit, 'comments':comments},
	)