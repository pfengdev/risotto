from django.http import HttpResponse
from django.template import loader
import spotipy
import spotipy.util as util
import logging

def index(request):
    template = loader.get_template('spotify/index.html')
    return HttpResponse(template.render({}, request))

def playlists_list(request):
    username = request.user.username
    spotify_client = get_spotify_client(request)
    playlists_response = spotify_client.user_playlists(username)
    template = loader.get_template('spotify/playlists_list.html')
    playlists = playlists_response['items']
    context = {
        'playlists': playlists
    }
    return HttpResponse(template.render(context, request))

def playlists_detail(request, playlist_id):
    username = request.user.username
    spotify_client = get_spotify_client(request)
    songs_response = spotify_client.user_playlist_tracks(username, playlist_id)
    songs = []
    for item in songs_response['items']:
        songs.append(item['track'])
    template = loader.get_template('spotify/playlists_detail.html')
    context = {
        'songs': songs
    }
    return HttpResponse(template.render(context, request))

def get_spotify_client(request):
    username = request.user.username
    social = request.user.social_auth.get(provider='spotify')
    token = social.extra_data['access_token']
    return spotipy.Spotify(auth = token)
