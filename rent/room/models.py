from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from image_optimizer.fields import OptimizedImageField


class Room(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, null=True, blank=True)
    tags = TaggableManager(blank=True)
    image = OptimizedImageField(upload_to='images/', optimized_image_resize_method='cover', blank=True, null=True)
    price = models.FloatField(blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='room_likes')
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        app_label = 'room'
        db_table = 'room_room'

class Images(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = OptimizedImageField(upload_to='images/', optimized_image_resize_method='cover', blank=True, null=True)
    class Meta:
        managed = True
        app_label = 'room'
        db_table = 'room_images'

class RoomComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class RoomViewsTracker(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)