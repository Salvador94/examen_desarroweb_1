from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import LibroListAPIView, LibroCreateAPIView

urlpatterns=[
    url(r'^$', LibroListAPIView.as_view(), name = 'list'),
    url(r'^create/$', LibroCreateAPIView.as_view(), name='create'),

]
