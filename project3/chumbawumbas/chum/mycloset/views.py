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
	user1 = UserProfile.objects.get(user__username = 'Tim Richards')
	user2 = UserProfile.objects.get(user__username = 'Bob')
	user3 = UserProfile.objects.get(user__username = 'Michelle')
	num_user = User.objects.all().count()

	return render(
		request,
		'friends.html',
		context={'num_user':num_user,'user_one':user1, 'user_two':user2, 'user_three':user3},
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

#@permission_required('catalog.can_mark_returned')
def update_profile(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    user_profile=get_object_or_404(UserProfile, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UpdateProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_profile.residence = form.cleaned_data['new_residence']
            user_profile.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profile') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_residence = user_profile.residence
        form = UpdateProfileForm(initial={'new_residence': proposed_residence,})

    return render(request, 'mycloset/update_profile.html', {'form': form, 'user_profile':user_profile})