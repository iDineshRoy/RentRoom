from django.urls import path
from .views import search_view, tagged, quick_search

urlpatterns = [
    path('',search_view),
    path('now/', quick_search),
    path('search/',search_view),
    path('tag/<slug:slug>', tagged, name='tagged'),
]