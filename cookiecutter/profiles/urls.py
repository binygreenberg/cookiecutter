from django.conf.urls import url
from .views import ProfileListView

urlpatterns = [
    url(r'^all/$', ProfileListView.as_view(), name='profiles-all'),
]
