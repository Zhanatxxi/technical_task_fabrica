from django.contrib import admin

from src.account.models import CustomUser, UserProfile

admin.site.register(CustomUser)
admin.site.register(UserProfile)