from django.urls import path

from . import views

app_name = 'spotify'
urlpatterns = [
    path('playlists', views.get_playlists, name = 'playlists')
]
