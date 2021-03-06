from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Clothing, ClothingType, Outfit, Comment, Weather, UserProfile

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
	user_profile = UserProfile.objects.get(user=request.user)
	closet_clothing = Outfit.objects.all()
	types = ClothingType.objects.get(type_name = "Skirt")
	specific_outfit = Outfit.objects.get(outfit_name = "Formal")
	specific_weather = Weather.objects.get(weather_type = "Cloudy")

	return render(
		request,
		'closet.html',
		context={'user_profile': user_profile, 'closet_clothing':closet_clothing, 'types':types, 'specific_outfit':specific_outfit, 'specific_weather':specific_weather}
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
	previous_outfits = Outfit.objects.filter(user=request.user)[:3]
	favorite_outfits = Outfit.objects.filter(user=request.user).filter(favorite='Y')


	return render(
		request,
		'profile.html',
		context = {'user_profile':user_profile, 'previous_outfits':previous_outfits, 'favorite_outfits':favorite_outfits},
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


#from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import UpdateProfileForm
from .forms import AddClothingForm

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
			clothing = Clothing.objects.create(clothing_name=form.cleaned_data['new_clothing_name'], clothing_type=form.cleaned_data['new_clothing_type'], clothing_picture=form.cleaned_data['new_clothing_picture'], weather=form.cleaned_data['new_weather_type'])
			user_profile.closet.add(clothing)
			user_profile.save()

			return HttpResponseRedirect(reverse('closet'))

	else:
		form = AddClothingForm()

	return render(request, 'mycloset/add_clothing.html', {'form': form, 'user_profile': user_profile})
