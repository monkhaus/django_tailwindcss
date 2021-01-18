from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
	path('login/', views.loginPage, name='loginPage'),
	path('logout/', views.logoutUser, name='logoutUser'),
	path('register/', views.registerPage, name='registerPage'),
]

