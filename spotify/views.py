from django.http import HttpResponse
from django.template import loader
import jieba
import logging
import lyricsgenius
import spotipy
import spotipy.util as util

def index(request):
    template = loader.get_template('spotify/index.html')
    return HttpResponse(template.render({}, request))

def genius(request):
    template = loader.get_template('spotify/genius.html')
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
        song = item['track']
        song['search_artist'] = song['artists'][0]['name']
        songs.append(item['track'])
    template = loader.get_template('spotify/playlists_detail.html')
    context = {
        'songs': songs
    }
    return HttpResponse(template.render(context, request))

def song_lyrics(request, search_artist, song_name):
    username = request.user.username
    genius_client = get_genius_client(request)
    song = genius_client.search_song(song_name, search_artist)
    song_lyrics_full_text = song.lyrics
    song_lines = []
    for line in song_lyrics_full_text.split('\n'):
        song_words = jieba.cut(line, cut_all=False)
        song_lines.append(song_words)
    template = loader.get_template('spotify/song_lyrics.html')
    context = {
        'song_name': song_name,
        'song_lines': song_lines
    }
    return HttpResponse(template.render(context, request))

def get_spotify_client(request):
    username = request.user.username
    spotify_social = request.user.social_auth.get(provider='spotify')
    token = spotify_social.extra_data['access_token']
    return spotipy.Spotify(auth = token)

def get_genius_client(request):
    username = request.user.username
    genius_social = request.user.social_auth.get(provider='genius')
    token = genius_social.extra_data['access_token']
    return lyricsgenius.Genius(client_access_token=token)
