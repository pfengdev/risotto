from django.urls import path

from . import views

app_name = 'spotify'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('playlists', views.playlists_list, name = 'playlists_list'),
    path('playlists/<str:playlist_id>/songs', views.playlists_detail, name = 'playlists_detail')
]
