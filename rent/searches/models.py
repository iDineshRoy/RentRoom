from django.db import models
from django.contrib.auth.models import User


class RoomSearchQuery(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)