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

def game(request):
    template_data = {}
    template_data['title'] = "Game"
    songList = [
    ## 90s songs ##
    Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path='/static/mp3s/LifeIsAHighwayTomCochrane.mp3', category="90s"),
    Song(title="All Star", artist="Smash Mouth", year=1999, album="Astro Lounge", path='/static/mp3s/All-Star-Smash-Mouth.mp3', category="90s"),
    Song(title="Virtual Insanity", artist="Jamiroquai", year=1996, album="Travelling Without Moving", path='/static/mp3s/Virtual-Insanity-Jamiroquai.mp3', category="90s"),

    ## 80s songs ##
    Song(title="Everybody Wants to Rule the World", artist="Tears for Fears", year=1985, album="Songs from the Big Chair", path='/static/mp3s/Everybody-Wants-To-Rule-The-World-Tears-For-Fears.mp3', category="80s"),
    Song(title="I'm Still Standing", artist="Elton John", year=1983, album="Too Low for Zero", path='/static/mp3s/Im-Still-Standing-Elton-John.mp3', category="80s"),

    ## 2000s songs ##
    Song(title="Lose Yourself", artist="Eminem", year=2002, album="", path='/static/mp3s/2000s/Eminem - Lose Yourself.mp3', category="2000s"),
    Song(title="Party Rock Anthem", artist="LMFAO", year=2010, album="", path='/static/mp3s/2000s/LMFAO ft. Lauren Bennett, GoonRock - Party Rock Anthem (Official Audio).mp3', category="2000s"),
    Song(title="Thrift Shop", artist="Macklemore", year=2012, album="", path='/static/mp3s/2000s/MACKLEMORE & RYAN LEWIS - THRIFT SHOP FEAT. WANZ (OFFICIAL VIDEO).mp3', category="2000s"),
    Song(title="Bartender", artist="T-Pain", year=2007, album="", path='/static/mp3s/2000s/T-Pain - Bartender (Official HD Video) ft. Akon.mp3', category="2000s"),
    Song(title="Pump It", artist="The Black Eyed Peas", year=2005, album="", path='/static/mp3s/2000s/The Black Eyed Peas - Pump It (Official Music Video).mp3', category="2000s"),

    ## dad rock songs ##
    Song(title="Higher", artist="Creed", year=1999, album="", path='/static/mp3s/dad rock/Creed - Higher (Remastered) (Official Audio).mp3', category="dad rock"),
    Song(title="My Sacrifice", artist="Creed", year=2001, album="", path='/static/mp3s/dad rock/Creed - My Sacrifice.mp3', category="dad rock"),
    Song(title="Everlong", artist="Foo Fighters", year=1997, album="", path='/static/mp3s/dad rock/Foo Fighters - Everlong (Official HD Video).mp3', category="dad rock"),
    Song(title="How You Remind Me", artist="Nickelback", year=2001, album="", path='/static/mp3s/dad rock/Nickelback - How You Remind Me [OFFICIAL VIDEO].mp3', category="dad rock"),
    Song(title="Heart-Shaped Box", artist="Nirvana", year=1993, album="", path='/static/mp3s/dad rock/Nirvana - Heart-Shaped Box (Official Music Video).mp3', category="dad rock"),
    Song(title="Creep", artist="Radiohead", year=1992, album="", path='/static/mp3s/dad rock/Radiohead - Creep.mp3', category="dad rock"),

    ## girl pop songs ##
    Song(title="BIRDS OF A FEATHER", artist="Billie Eilish", year=2024, album="", path='/static/mp3s/girl pop/Billie Eilish - BIRDS OF A FEATHER (Official Lyric Video).mp3', category="girl pop"),
    Song(title="Apple", artist="Charli xcx", year=2024, album="", path='/static/mp3s/girl pop/Charli xcx - Apple (official lyric video).mp3', category="girl pop"),
    Song(title="HOT TO GO!", artist="Chappell Roan", year=2023, album="", path='/static/mp3s/girl pop/HOT TO GO! (Audio) - Chappell Roan.mp3', category="girl pop"),
    Song(title="Espresso", artist="Sabrina Carpenter", year=2024, album="", path='/static/mp3s/girl pop/Sabrina Carpenter - Espresso (Official Audio).mp3', category="girl pop"),
    Song(title="Wildest Dreams", artist="Taylor Swift", year=2014, album="", path='/static/mp3s/girl pop/Taylor Swift - Wildest Dreams.mp3', category="girl pop"),

    ## opium songs ##
    Song(title="if looks could kill", artist="Destroy Lonely", year=2023, album="", path='/static/mp3s/opium/Destroy Lonely - if looks could kill (Official Audio).mp3', category="opium"),
    Song(title="Uzi Work", artist="Homixide Gang", year=2023, album="", path='/static/mp3s/opium/Homixide Gang - Uzi Work (Official Audio) [prod by KP].mp3', category="opium"),
    Song(title="ss", artist="Ken Carson", year=2023, album="", path='/static/mp3s/opium/ss.mp3', category="opium"),
    Song(title="Shoota", artist="Playboi Carti", year=2018, album="", path='/static/mp3s/opium/Playboi-Carti-Shoota.mp3', category="opium"),
    Song(title="Magnolia", artist="Playboi Carti", year=2017, album="", path='/static/mp3s/opium/Playboi Carti - Magnolia (Audio).mp3', category="opium"),
    #Song(title="Shoota", artist="Playboi Carti", year=2018, album="", path='/static/mp3s/opium/Playboi Carti - Shoota (Audio) ft. Lil Uzi Vert.mp3', category="opium"),

    ## rap caviar songs ##
    Song(title="Tweaker", artist="GELO", year=2025, album="", path='/static/mp3s/rap caviar/G3 (LiAngelo Ball) - Tweaker (Official Audio).mp3', category="rap caviar"),
    Song(title="tv off", artist="Kendrick Lamar", year=2024, album="", path='/static/mp3s/rap caviar/Kendrick Lamar - tv off (Official Audio).mp3', category="rap caviar"),
    Song(title="NOKIA", artist="Drake", year=2025, album="", path='/static/mp3s/rap caviar/NOKIA.mp3', category="rap caviar"),
    Song(title="Timeless", artist="The Weeknd", year=2024, album="", path='/static/mp3s/rap caviar/The Weeknd  Timeless with Playboi Carti (Official Music Video).mp3', category="rap caviar"),
    Song(title="MELTDOWN", artist="Travis Scott", year=2023, album="", path='/static/mp3s/rap caviar/Travis Scott - MELTDOWN (Official Audio) ft. Drake.mp3', category="rap caviar"),

    ]
<<<<<<< HEAD
        
=======
    
>>>>>>> feature/Websites
    category = request.GET.get('category', 'all')

    # Filter songs by category if specified
    if category != 'all':
        songList = [song for song in songList if song.category == category]

    song = random.choice(songList) if songList else None
    return render(request, 'game.html', {
        'template_data': template_data,
        'song': song
    })



def pregame(request):
    template_data = {}
    template_data['title'] = "Pregame"
    categories = ["80s", "90s", "2000s", "dad rock", "girl pop", "opium", "rap caviar", "all"]
    return render(request, 'pregame.html', {
        'template_data': template_data,
        'categories': categories
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
    return render(request, 'signup.html', {
        'template_data': template_data
    })

# NEW ADDITION
def login(request):
    template_data = {}
    template_data['title'] = "Log In"
    return render(request, 'login.html', {
        'template_data': template_data
    })

def logout(request):
    del request.session["username"]

    return redirect(reverse("user.login"))


#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })
