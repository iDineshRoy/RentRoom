from django.contrib import admin
from django.urls import path
from .views import contact, success

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', success, name='success'),
]
