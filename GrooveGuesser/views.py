from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from user.models import Account #This should give this file access to the model Account in \user\models.py
from .models import Round

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

def pregame(request):
    template_data = {}
    template_data['title'] = "Enter Game"
    playerName = request.session.get('playerName', '')
    return render(request, 'pregame.html', {
        'template_data': template_data,
        'playerName': playerName
    })

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    playerName = request.session.get('playerName', '')
    return render(request, 'game.html', {
        'template_data': template_data,
        'playerName': playerName
    })
    

def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    accounts = Account.objects.all()
    newRound = Round(player="newplayer", score=1)
    allRounds = Round.objects.all()
    return render(request, 'leaderboard.html', {
        'template_data': template_data,
        'accounts': accounts,
        'gameRound': newRound,
        'allRounds': allRounds
    })

#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })