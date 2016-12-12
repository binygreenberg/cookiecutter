# encoding: utf-8
from django.conf.urls import url
from .views import (
        BasicVersionCreateView, BasicPlusVersionCreateView,
        jQueryVersionCreateView, AngularVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = [
    # url(r'^basic/$', BasicVersionCreateView.as_view(), name='upload-basic'),
    # url(r'^basic/plus/$', BasicPlusVersionCreateView.as_view(), name='upload-basic-plus'),
    url(r'^new/$', PictureCreateView.as_view(), name='upload-new'),
    # url(r'^angular/$', AngularVersionCreateView.as_view(), name='upload-angular'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
]
