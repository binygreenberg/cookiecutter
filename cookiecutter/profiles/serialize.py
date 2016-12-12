from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)


    class Meta:
        model = Profile
        fields = ('description','location','images')
