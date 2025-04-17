from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse
import random
import time
import os
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from .models import Song
from user.models import Account #This should give this file access to the model Account in \user\models.py
from .models import Round
from django.db.models import Avg

#grooveguesser test responses
def index(request):
    # return HttpResponse("Hello, Welcome to the GrooveGuesser app.") (WIP PF)
    template_data = {}
    template_data['title'] = "Home Page"
    username = request.session.get('username', '')
    return render(request, 'GrooveGuesser.html', {
        'template_data': template_data,
        'username': username
    })

def about(request):
    # return HttpResponse("GrooveGuesser is a song guessing game.") (WIP PF)
    template_data = {}
    template_data['title'] = "About"
    username = request.session.get('username', '')
    return render(request, 'about.html', {
        'template_data': template_data,
        'username': username
    })

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    songList = [
        Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path='/static/mp3s/LifeIsAHighwayTomCochrane.mp3', category="90s"),
        Song(title="All Star", artist="Smash Mouth", year=1999, album="Astro Lounge", path='/static/mp3s/All-Star-Smash-Mouth.mp3', category="90s"),

        Song(title="Everybody Wants to Rule the World", artist="Tears for Fears", year=1985, album="Songs from the Big Chair", path='/static/mp3s/Everybody-Wants-To-Rule-The-World-Tears-For-Fears.mp3', category="80s"),
        Song(title="I'm Still Standing", artist="Elton John", year=1983, album="Too Low for Zero", path='/static/mp3s/Im-Still-Standing-Elton-John.mp3', category="80s"),
        
        Song(title="Virtual Insanity", artist="Jamiroquai", year=1996, album="Travelling Without Moving", path='/static/mp3s/Virtual-Insanity-Jamiroquai.mp3', category="90s"),
    ]
    
    category = request.GET.get('category', 'all')

    # Filter songs by category if specified
    if category != 'all':
        songList = [song for song in songList if song.category == category]

    username = request.session.get('username', '')
    song = random.choice(songList) if songList else None
    return render(request, 'game.html', {
        'template_data': template_data,
        'song': song,
        'username': username
    })



def pregame(request):
    template_data = {}
    template_data['title'] = "Pregame"
    categories = ["80s", "90s", "2000s", "all"]
    username = request.session.get('username', '')
    return render(request, 'pregame.html', {
        'template_data': template_data,
        'categories': categories,
        'username': username
    })


    

def leaderboard(request):
    template_data = {}
    template_data['title'] = "Leaderboard"
    accounts = Account.objects.all()
    newRound = Round(player="newplayer", score=1)
    allRounds = Round.objects.all()
    username = request.session.get('username', '')

    avg_scores = []

    for account in accounts:
        theirRounds = Round.objects.filter(player=account.username)

        sum_scores = sum(round.score for round in theirRounds)

        average_score = sum_scores / len(theirRounds) if theirRounds else 0

        avg_scores.append({
            'username': account.username,
            'average': round(average_score, 2)
        })
    

    return render(request, 'leaderboard.html', {
        'template_data': template_data,
        'accounts': accounts,
        'gameRound': newRound,
        'allRounds': allRounds,
        'username': username,
        'avg_scores': avg_scores,
    })


# This used to be in leaderboard, creates errors without Round model
# <!--  All Rounds Played -->
#     <h2 class="section-title">All Rounds Played</h2>
#     <div class="info-box">
#         {% for round in allRounds %}
#             <p><strong>{{ round.player }}</strong>: {{ round.score }}</p>
#         {% empty %}
#             <p class="empty-message">No rounds played yet.</p>
#         {% endfor %}
#     </div>

def audio_player(request):
    return render(request, 'audio_player.html')

# NEW ADDITION
def signup(request):
    template_data = {}
    template_data['title'] = "Sign Up"
    username = request.session.get('username', '')
    return render(request, 'signup.html', {
        'template_data': template_data,
        'username': username,
    })


def logout(request):
    del request.session["username"]

    return redirect(reverse("user.login"))


#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })


def add_round(request):
    if request.method == 'POST':
        username = request.session.get('username', '')

        if username != '':
            Round.objects.create(player=username, score=10)
            return JsonResponse({'success': True, 'roundFor': username}, 200)
        else:
            return JsonResponse({'success': True}, 200)
    
    else:
        return JsonResponse({'success': False}, 400)

