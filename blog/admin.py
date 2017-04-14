# blog/admin.py
from django.contrib import admin
from .models import Post


# admi.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']


admin.site.register(Post, PostAdmin)