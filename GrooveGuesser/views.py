from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import time
from django.conf import settings
from googleapiclient.discovery import build
from django.shortcuts import render
from .models import Song

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
    song = Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path='\static\mp3s\LifeIsAHighwayTomCochrane.mp3')
    return render(request, 'game.html', {
        'template_data': template_data,
        'song': song
    })

def get_video_details(video_id):

    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    
    return None


def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    return render(request, 'leaderboard.html', {
        'template_data': template_data
    })
