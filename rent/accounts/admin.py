from django.contrib import admin

from .models import UserDetails, Comments, ViewsTracker
admin.site.register(UserDetails)
admin.site.register(Comments)
admin.site.register(ViewsTracker)