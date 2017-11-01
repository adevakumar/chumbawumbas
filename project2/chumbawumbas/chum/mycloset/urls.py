from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.closet, name='closet'),
	url(r'^$', views.profile, name ='profile'),
	url(r'^$', views.friends, name ='friends'),

]
