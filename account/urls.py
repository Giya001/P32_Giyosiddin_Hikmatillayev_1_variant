from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path,include

from account import views
from django.contrib.auth import views as auth_views
from account import views as account_views
urlpatterns = [
    path('register/',account_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
]
