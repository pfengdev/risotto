from django.http import HttpResponse
import spotipy
import spotipy.util as util
import logging

def get_playlists(request):
    return HttpResponse('playlists')
