from .models import Profile
from rest_framework import generics
from .serialize import ProfileSerializer
from .models import Profile
# Create your views here.

class ProfileListView(generics.ListAPIView):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
