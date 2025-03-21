from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
from django.urls import reverse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from user.models import Account #This should give this file access to the model Account in \user\models.py
from .models import Round

#grooveguesser test responses
def index(request):
    # return HttpResponse("Hello, Welcome to the GrooveGuesser app.") (WIP PF)
    template_data = {}
    template_data['title'] = "Home Page"
    username = request.session.get('username')
    return render(request, 'GrooveGuesser.html', {
        'template_data': template_data,
        'username': username
    })

def about(request):
    # return HttpResponse("GrooveGuesser is a song guessing game.") (WIP PF)
    template_data = {}
    template_data['title'] = "About"
    username = request.session.get('username')
    return render(request, 'about.html', {
        'template_data': template_data,
        'username': username
    })

def pregame(request):
    template_data = {}
    template_data['title'] = "Enter Game"
    username = request.session.get('username', '')
    return render(request, 'pregame.html', {
        'template_data': template_data,
        'username': username
    })

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    
    practice = False
    data = request.GET.get('data')
    username = request.session.get('username', '')
    if data == 'p':
        practice = True

    return render(request, 'game.html', {
        'template_data': template_data,
        'username': username,
        'practice': practice
    })
    

def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    accounts = Account.objects.all()
    newRound = Round(player="newplayer", score=1)
    allRounds = Round.objects.all()
    username = request.session.get('username', '')
    return render(request, 'leaderboard.html', {
        'template_data': template_data,
        'accounts': accounts,
        'gameRound': newRound,
        'allRounds': allRounds,
        'username': username
    })


def logout(request):
    del request.session["username"]

    return redirect(reverse("user.login"))

#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })