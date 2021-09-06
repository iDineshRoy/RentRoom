from django.urls import path, include
from accounts.views import (
    showusers, register, profile, province1, userinfo, logout_view, signin, updatedetails, showterms, changepassword, addemail, showprivacy, deletecomment, likeuser, enternumber, otpprocess
)
from django.contrib.auth import views

urlpatterns = [
    path('',showusers),
    path('register/', register),
    path('profile/', profile),
    path('user/<str:id>', userinfo),
    path('logout', logout_view),
    path('login', signin),
    path('profile-update/<str:id>', updatedetails),#changes here as well
    path('terms', showterms, name='terms'),
    path('privacy', showprivacy, name='privacy'),
    path('changepwd/', changepassword),
    path('add-email', addemail),
    path('reg/', enternumber),
    path('enterotp/<int:otp>/<int:number>', otpprocess),
    path('comment/<int:id>/<int:userid>', deletecomment),
    path('like/<int:id>', likeuser, name="like_user"),
    path('reset_password/', views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]