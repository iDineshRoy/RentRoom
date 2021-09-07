from django.urls import path, include
from .views import homepage, create_product, show_product, edit_product, update_more_details, upload_pics, like_product, delete_pictures, add_more_details
from django.contrib.auth import views

urlpatterns = [
    path('', homepage, name='home'),
    path('new_room', create_product, name='new_product'),
    path('room/<int:id>', show_product, name='show_product'),
    path('edit_room/<int:id>', edit_product, name='edit_product'),
    path('add_pics/<int:id>', upload_pics, name='add_pics'),
    path('like/<int:id>', like_product, name='like_product'),
    path('delete_pics/<int:id>', delete_pictures, name='delete_pics'),
    path('more-details-add/<str:id>', add_more_details, name='add-more'),
    path('more-details-update/<str:id>', update_more_details, name='update-more'),
]