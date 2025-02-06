from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#grooveguesser test responses
def index(request):
    # return HttpResponse("Hello, Welcome to the GrooveGuesser app.") (WIP PF)
    template_data = {}
    template_data['title'] = "Home Page"
    return render(request, 'GrooveGuesser.html', {
        'template_data': template_data
    })

def about(request):
    # return HttpResponse("GrooveGuesser is a song guessing game.") (WIP PF)
    template_data = {}
    template_data['title'] = "About"
    return render(request, 'about.html', {
        'template_data': template_data
    })

def get_random_song():
    """Fetch a random song preview URL and its metadata."""
    playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # Top 50 Global Playlist
    tracks = sp.playlist_tracks(playlist_id)["items"]
    
    random_track = random.choice(tracks)
    song_name = random_track["track"]["name"]
    artist = random_track["track"]["artists"][0]["name"]
    preview_url = random_track["track"]["preview_url"]

    return {"song_name": song_name, "artist": artist, "preview_url": preview_url}

    



#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })