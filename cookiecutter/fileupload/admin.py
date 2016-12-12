from .models import Picture
from django.contrib import admin

@admin.register(Picture)
class MyPictureAdmin(admin.ModelAdmin):
    list_display = ('profile','slug','file')
