from django.urls import path

from . import views

app_name = 'spotify'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('playlists', views.get_playlists, name = 'playlists')
]
