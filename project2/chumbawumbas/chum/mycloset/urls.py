from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^closet.html$', views.closet, name='closet'),
	url(r'^profile.html$', views.profile, name='profile'),
	url(r'^friends.html$', views.friends, name='friends'),
	url(r'^weather.html$', views.weather, name='weather'),
	url(r'^fifth.html$', views.about, name='about'),
]
