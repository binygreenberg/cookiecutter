from .models import Profile
from django.contrib import admin

@admin.register(Profile)
class MyPictureAdmin(admin.ModelAdmin):
    list_display = ('user','description','id')
