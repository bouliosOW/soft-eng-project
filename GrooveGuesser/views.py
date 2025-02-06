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

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    return render(request, 'game.html', {
        'template_data': template_data
    })
    



#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })