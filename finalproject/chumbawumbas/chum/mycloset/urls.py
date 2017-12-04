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

urlpatterns += [   
    url(r'^profile/(?P<pk>[-\w]+)/update/$', views.update_profile, name='update-profile'),
    url(r'^closet/(?P<pk>[-\w]+)/add-clothing/$', views.add_clothing, name='add-clothing'),
    url(r'^closet/(?P<pk>[-\w]+)/add-outfit/$', views.add_outfit, name='add-outfit'),
    url(r'^profile/search/$', views.search_users, name='search-users'),
]