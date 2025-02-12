from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from googleapiclient.discovery import build
from django.shortcuts import render

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

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    return render(request, 'game.html', {
        'template_data': template_data
    })

def get_video_details(video_id):

    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    
    return None

def game(request):
    """View function to display a YouTube video in the game page."""
    
    video_id = "3JZ_D3ELwOQ" 
    video_details = get_video_details(video_id)
    
    print("Video Details:", video_details)

    return render(request, 'game.html', {"video_id": video_id, "video_details": video_details})
