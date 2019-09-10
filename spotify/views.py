from django.http import HttpResponse
from django.template import loader
import spotipy
import spotipy.util as util
import logging

def index(request):
    template = loader.get_template('spotify/index.html')
    return HttpResponse(template.render({}, request))

def get_playlists(request):
    return HttpResponse('playlists')
