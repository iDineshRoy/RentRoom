from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from .addressdetails import skillslist as sl

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    municipality = models.CharField(max_length=100, null=True)
    ward = models.IntegerField(null=True)
    skills = models.CharField(max_length=300, null=True)
    skilldetails = models.TextField(max_length=300, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='user_likes')


class Comments(models.Model):
    userdetails = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    content = models.TextField(max_length=400, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class ViewsTracker(models.Model):
    userdetails = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)