
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import time
import os
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


def game(request):
    random_mp3_file = getRandomMP3()

    return render(request, 'game.html', {"mp3_file": random_mp3_file})

def getRandomMP3():
    # Path to the 'mp3s' directory (adjust this as needed)
    mp3_folder = os.path.join(settings.BASE_DIR, 'static', 'mp3s')

    # Get a list of all MP3 files in the folder
    mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

    # Ensure there are MP3 files to select from
    if not mp3_files:
        return HttpResponse('No MP3 files found.', status=404)

    # Choose a random MP3 file
    random_mp3 = random.choice(mp3_files)

    # Construct the full file path
    mp3_file_path = os.path.join(mp3_folder, random_mp3)

    # Return the file as an HttpResponse
    with open(mp3_file_path, 'rb') as mp3_file:
        response = HttpResponse(mp3_file.read(), content_type='audio/mp3')
        response['Content-Disposition'] = f'attachment; filename="{random_mp3}"'
        return response

def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    return render(request, 'leaderboard.html', {'template_data': template_data})


def audio_player(request):
    return render(request, 'audio_player.html')