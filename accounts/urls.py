from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


urlpatterns = [
	path( '', views.home ),
	path( 'login/', login, {'template_name': 'accounts/login.html'} ),
	path( 'logout/', logout, {'template_name': 'accounts/logout.html'} ),
    path('register/', views.register, name='register'),
]