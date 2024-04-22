from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['name', 'username', 'role', 'is_staff']
    list_filter = ['role']


admin.site.register(CustomUser, CustomUserAdmin)
