from django.urls import path
from accounts.views import showusers, enternumber, otpprocess, signin, register, showterms, profile, userinfo, logout_view
from django.contrib.auth import views

urlpatterns = [
    path('',showusers),
    path('register/', register),
    path('profile/', profile, name='profile'),
    path('user/<str:id>', userinfo, name='show_user'),
    path('logout/', logout_view, name='logout'),
    path('login/', signin, name='login'),
    path('terms', showterms, name='terms'),
    path('sign-up/', enternumber, name='register'),
    path('enterotp/<int:otp>/<int:number>', otpprocess, name='enterotp'),
]