from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_verified','is_staff','is_active','is_superuser']
    list_filter = ['username']