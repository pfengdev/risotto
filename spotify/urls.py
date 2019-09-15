from django.urls import path

from . import views

app_name = 'spotify'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('genius', views.genius, name = 'genius'),
    path('playlists', views.playlists_list, name = 'playlists_list'),
    path('playlists/<str:playlist_id>/songs', views.playlists_detail, name = 'playlists_detail'),
    path('songs/<str:song_id>', views.song_lyrics, name = 'song_lyrics')
]
