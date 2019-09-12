from django.http import HttpResponse
from django.template import loader
import spotipy
import spotipy.util as util
import logging

def index(request):
    template = loader.get_template('spotify/index.html')
    return HttpResponse(template.render({}, request))

def get_playlists(request):
    username = request.user.username
    social = request.user.social_auth.get(provider='spotify')
    token = social.extra_data['access_token']
    spotify = spotipy.Spotify(auth = token)
    playlists = spotify.user_playlists(username)
    result = ""
    for item in playlists["items"]:
        result = result + item["name"]
    return HttpResponse(result)
