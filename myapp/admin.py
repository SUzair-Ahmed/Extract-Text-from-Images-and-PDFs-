# In admin.py
from django.contrib import admin
from .models import CustomUser
from myapp.models import UserSocialAuth

admin.site.register(CustomUser)


class UserSocialAuthAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid', 'guid')  # Ensure 'guid' is included in the list display
    fields = ('user', 'provider', 'uid', 'guid')  # Ensure 'guid' is included in the form

admin.site.register(UserSocialAuth, UserSocialAuthAdmin)