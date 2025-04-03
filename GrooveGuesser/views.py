
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import time
import os
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
    songList = [Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path='\static\mp3s\LifeIsAHighwayTomCochrane.mp3'),
                Song(title="All Star", artist="Smash Mouth", year=1999, album="Astro Lounge", path='\static\mp3s\All-Star-Smash-Mouth.mp3'),
                Song(title="Everybody Wants to Rule the World", artist="Tears for Fears", year=1985, album="Songs from the Big Chair", path='\static\mp3s\Everybody-Wants-To-Rule-The-World-Tears-For-Fears.mp3'),
                Song(title="I'm Still Standing", artist="Elton John", year=1983, album="Too Low for Zero", path='\static\mp3s\Im-Still-Standing-Elton-John.mp3'),
                Song(title="Virtual Insanity", artist="Jamiroquai", year=1996, album="Travelling Without Moving", path='\static\mp3s\Virtual-Insanity-Jamiroquai.mp3')]
    
    song=random.choice(songList)
    return render(request, 'game.html', {
        'template_data': template_data,
        'song': song
    })



def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    return render(request, 'leaderboard.html', {'template_data': template_data})


def audio_player(request):
    return render(request, 'audio_player.html')