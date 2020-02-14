from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.listing, name='store.listing'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='store.detail'),
    url(r'^search/$', views.search, name='store.search'),
]
