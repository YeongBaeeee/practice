# accounts/admin.py

from django.contrib import admin
from .models import Porfile


@admin.register(Porfile)
class ProfileAdmin(admin.ModelAdmin):
    pass


