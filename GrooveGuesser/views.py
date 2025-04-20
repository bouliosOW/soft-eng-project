import pdb
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
import json
from django.views.decorators.csrf import csrf_exempt

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

    ## 80s songs ## (12)
    Song(title="Everybody Wants to Rule the World", artist="Tears for Fears", year=1985, album="", path='/static/mp3s/80s/ewtrtw.mp3', category="80s"),
    Song(title="I'm Still Standing", artist="Elton John", year=1983, album="", path='/static/mp3s/80s/iss.mp3', category="80s"),
    Song(title="Billie Jean", artist="Michael Jackson", year=1983, album="", path='/static/mp3s/80s/billiejean.mp3', category="80s"),
    Song(title="Livin' On A Prayer", artist="Bon Jovi", year=1986, album="", path='/static/mp3s/80s/loap.mp3', category="80s"),
    Song(title="You Give Love A Bad Name", artist="Bon Jovi", year=1986, album="", path='/static/mp3s/80s/yglabn.mp3', category="80s"),
    Song(title="Everything She Wants", artist="George Michael", year=1984, album="", path='/static/mp3s/80s/shewants.mp3', category="80s"),
    Song(title="Careless Whisper", artist="George Michael", year=1984, album="", path='/static/mp3s/80s/careless.mp3', category="80s"),
    Song(title="I Want To Know What Love Is", artist="Foreigner", year=1984, album="", path='/static/mp3s/80s/whatloveis.mp3', category="80s"),
    Song(title="Danger Zone", artist="Kenny Loggins", year=1986, album="", path='/static/mp3s/80s/dangerzone.mp3', category="80s"),
    Song(title="Crazy Train", artist="Ozzy Osbourne", year=1980, album="", path='/static/mp3s/80s/crazytrain.mp3', category="80s"),
    Song(title="Under Pressure", artist="Queen", year=1981, album="", path='/static/mp3s/80s/underp.mp3', category="80s"),
    Song(title="Never Gonna Give You Up", artist="Rick Astley", year=1987, album="", path='/static/mp3s/80s/nggyu.mp3', category="80s"),

    ## 90s songs ## (11)
    Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="", path='/static/mp3s/90s/liahw.mp3', category="90s"),
    Song(title="All Star", artist="Smash Mouth", year=1999, album="", path='/static/mp3s/90s/as.mp3', category="90s"),
    Song(title="Virtual Insanity", artist="Jamiroquai", year=1996, album="", path='/static/mp3s/90s/virtual.mp3', category="90s"),
    Song(title="Song 2", artist="Blur", year=1997, album="", path='/static/mp3s/90s/song.mp3', category="90s"),
    Song(title="Zombie", artist="The Cranberries", year=1994, album="", path='/static/mp3s/90s/zombie.mp3', category="90s"),
    Song(title="Mr. Jones", artist="Counting Crows", year=1993, album="", path='/static/mp3s/90s/mrjones.mp3', category="90s"),
    Song(title="My Hero", artist="Foo Fighters", year=1997, album="", path='/static/mp3s/90s/myhero.mp3', category="90s"),
    Song(title="Kiss Me", artist="Sixpence None The Richer", year=1997, album="", path='/static/mp3s/90s/kissme.mp3', category="90s"),
    Song(title="Push", artist="Matchbox Twenty", year=1997, album="", path='/static/mp3s/90s/push.mp3', category="90s"),
    Song(title="Iris", artist="Goo Goo Dolls", year=1998, album="", path='/static/mp3s/90s/iris.mp3', category="90s"),
    Song(title="Under The Bridge", artist="Red Hot Chili Peppers", year=1992, album="", path='/static/mp3s/90s/bridge.mp3', category="90s"),

    ## 2000s songs ## (14)
    Song(title="Lose Yourself", artist="Eminem", year=2002, album="", path='/static/mp3s/2000s/ly.mp3', category="2000s"),
    Song(title="Party Rock Anthem", artist="LMFAO", year=2010, album="", path='/static/mp3s/2000s/pra.mp3', category="2000s"),
    Song(title="Thrift Shop", artist="Macklemore", year=2012, album="", path='/static/mp3s/2000s/ts.mp3', category="2000s"),
    Song(title="Bartender", artist="T-Pain", year=2007, album="", path='/static/mp3s/2000s/bartender.mp3', category="2000s"),
    Song(title="Pump It", artist="The Black Eyed Peas", year=2005, album="", path='/static/mp3s/2000s/pumpit.mp3', category="2000s"),
    Song(title="Airplanes", artist="B.o.B", year=2010, album="", path='/static/mp3s/2000s/airplanes.mp3', category="2000s"),
    Song(title="Grenade", artist="Bruno Mars", year=2010, album="", path='/static/mp3s/2000s/grenade.mp3', category="2000s"),
    Song(title="Viva La Vida", artist="Coldplay", year=2008, album="", path='/static/mp3s/2000s/vivalavida.mp3', category="2000s"),
    Song(title="Low", artist="Flo Rida", year=2008, album="", path='/static/mp3s/2000s/low.mp3', category="2000s"),
    Song(title="Stereo Hearts", artist="Gym Class Heroes", year=2011, album="", path='/static/mp3s/2000s/stereohearts.mp3', category="2000s"),
    Song(title="Give Me Everything", artist="Pitbull", year=2011, album="", path='/static/mp3s/2000s/givemeeverything.mp3', category="2000s"),
    Song(title="Some Nights", artist="fun.", year=2012, album="", path='/static/mp3s/2000s/somenights.mp3', category="2000s"),
    Song(title="Hey, Soul Sister", artist="Train", year=2009, album="", path='/static/mp3s/2000s/soulsister.mp3', category="2000s"),
    Song(title="Yeah!", artist="Usher", year=2004, album="", path='/static/mp3s/2000s/yeah.mp3', category="2000s"),

    ## dad rock songs ## (12)
    Song(title="Higher", artist="Creed", year=1999, album="", path='/static/mp3s/dadrock/higher.mp3', category="dad rock"),
    Song(title="My Sacrifice", artist="Creed", year=2001, album="", path='/static/mp3s/dadrock/mysacrifice.mp3', category="dad rock"),
    Song(title="Everlong", artist="Foo Fighters", year=1997, album="", path='/static/mp3s/dadrock/everlong.mp3', category="dad rock"),
    Song(title="How You Remind Me", artist="Nickelback", year=2001, album="", path='/static/mp3s/dadrock/hyrm.mp3', category="dad rock"),
    Song(title="Heart-Shaped Box", artist="Nirvana", year=1993, album="", path='/static/mp3s/dadrock/hsb.mp3', category="dad rock"),
    Song(title="Creep", artist="Radiohead", year=1992, album="", path='/static/mp3s/dadrock/creep.mp3', category="dad rock"),
    Song(title="Enter Sandman", artist="Metallica", year=1991, album="", path='/static/mp3s/dadrock/sandman.mp3', category="dad rock"),
    Song(title="Brain Stew", artist="Green Day", year=1995, album="", path='/static/mp3s/dadrock/brainstew.mp3', category="dad rock"),
    Song(title="Master Of Puppets", artist="Metallica", year=1986, album="", path='/static/mp3s/dadrock/puppets.mp3', category="dad rock"),
    Song(title="Scar Tissue", artist="Red Hot Chili Peppers", year=1999, album="", path='/static/mp3s/dadrock/scartissue.mp3', category="dad rock"),
    Song(title="Shot in the Dark", artist="Ozzy Osbourne", year=1986, album="", path='/static/mp3s/dadrock/shotdark.mp3', category="dad rock"),
    Song(title="The Chain", artist="Fleetwood Mac", year=1977, album="", path='/static/mp3s/dadrock/chain.mp3', category="dad rock"),

    ## girl pop songs ## (10)
    Song(title="BIRDS OF A FEATHER", artist="Billie Eilish", year=2024, album="", path='/static/mp3s/girlpop/boaf.mp3', category="girl pop"),
    Song(title="Apple", artist="Charli xcx", year=2024, album="", path='/static/mp3s/girlpop/charliccc.mp3', category="girl pop"),
    Song(title="HOT TO GO!", artist="Chappell Roan", year=2023, album="", path='/static/mp3s/girlpop/hottogo.mp3', category="girl pop"),
    Song(title="Espresso", artist="Sabrina Carpenter", year=2024, album="", path='/static/mp3s/girlpop/espresso.mp3', category="girl pop"),
    Song(title="Wildest Dreams", artist="Taylor Swift", year=2014, album="", path='/static/mp3s/girlpop/wildestdreams.mp3', category="girl pop"),
    Song(title="A Thousand Miles", artist="Vanessa Carlton", year=2001, album="", path='/static/mp3s/girlpop/thousand.mp3', category="girl pop"),
    Song(title="Into You", artist="Ariana Grande", year=2016, album="", path='/static/mp3s/girlpop/intoyou.mp3', category="girl pop"),
    Song(title="Poker Face", artist="Lady Gaga", year=2008, album="", path='/static/mp3s/girlpop/pokerface.mp3', category="girl pop"),
    Song(title="deja vu", artist="Olivia Rodrigo", year=2021, album="", path='/static/mp3s/girlpop/oliviarodrigo.mp3', category="girl pop"),
    Song(title="22", artist="Taylor Swift", year=2013, album="", path='/static/mp3s/girlpop/twentytwo.mp3', category="girl pop"),

    ## opium songs ## (13)
    Song(title="if looks could kill", artist="Destroy Lonely", year=2023, album="", path='/static/mp3s/opium/ilck.mp3', category="opium"),
    Song(title="Uzi Work", artist="Homixide Gang", year=2023, album="", path='/static/mp3s/opium/uziwork.mp3', category="opium"),
    Song(title="ss", artist="Ken Carson", year=2023, album="", path='/static/mp3s/opium/ss.mp3', category="opium"),
    Song(title="Shoota", artist="Playboi Carti", year=2018, album="", path='/static/mp3s/opium/shoota.mp3', category="opium"),
    Song(title="Magnolia", artist="Playboi Carti", year=2017, album="", path='/static/mp3s/opium/magnolia.mp3', category="opium"),
    Song(title="how u feel", artist="Destroy Lonely", year=2023, album="", path='/static/mp3s/opium/howufeel.mp3', category="opium"),
    Song(title="NOSTYLIST", artist="Destroy Lonely", year=2022, album="", path='/static/mp3s/opium/nostylist.mp3', category="opium"),
    Song(title="Yale", artist="Ken Carson", year=2020, album="", path='/static/mp3s/opium/yale.mp3', category="opium"),
    Song(title="Blakk Rokkstar", artist="Ken Carson", year=2025, album="", path='/static/mp3s/opium/rokkstar.mp3', category="opium"),
    Song(title="overseas", artist="Ken Carson", year=2023, album="", path='/static/mp3s/opium/overseas.mp3', category="opium"),
    Song(title="No Time", artist="Playboi Carti", year=2018, album="", path='/static/mp3s/opium/notime.mp3', category="opium"),
    Song(title="EVIL J0RDAN", artist="Playboi Carti", year=2025, album="", path='/static/mp3s/opium/jordan.mp3', category="opium"),
    Song(title="Sky", artist="Playboi Carti", year=2021, album="", path='/static/mp3s/opium/sky.mp3', category="opium"),

    ## rap caviar songs ## (10)
    Song(title="Tweaker", artist="GELO", year=2025, album="", path='/static/mp3s/rapcaviar/tweaker.mp3', category="rap caviar"),
    Song(title="tv off", artist="Kendrick Lamar", year=2024, album="", path='/static/mp3s/rapcaviar/tvoff.mp3', category="rap caviar"),
    Song(title="NOKIA", artist="Drake", year=2025, album="", path='/static/mp3s/rapcaviar/nokia.mp3', category="rap caviar"),
    Song(title="Timeless", artist="The Weeknd", year=2024, album="", path='/static/mp3s/rapcaviar/timeless.mp3', category="rap caviar"),
    Song(title="MELTDOWN", artist="Travis Scott", year=2023, album="", path='/static/mp3s/rapcaviar/meltdown.mp3', category="rap caviar"),
    Song(title="Like That", artist="Future", year=2024, album="", path='/static/mp3s/rapcaviar/likethat.mp3', category="rap caviar"),
    Song(title="GIMME A HUG", artist="Drake", year=2025, album="", path='/static/mp3s/rapcaviar/gimmeahug.mp3', category="rap caviar"),
    Song(title="Outfit", artist="Lil Baby", year=2025, album="", path='/static/mp3s/rapcaviar/outfit.mp3', category="rap caviar"),
    Song(title="Dark Thoughts", artist="Lil Tecca", year=2025, album="", path='/static/mp3s/rapcaviar/thoughts.mp3', category="rap caviar"),
    Song(title="4X4", artist="Travis Scott", year=2025, album="", path='/static/mp3s/rapcaviar/fourxfour.mp3', category="rap caviar"),

    ## throwback ## (17)
    Song(title="Mr.Saxobeat", artist="Alexandra Stan", year=2011, album="", path='/static/mp3s/throwback/saxobeat.mp3', category="throwback"),
    Song(title="Safe And Sound", artist="Capital Cities", year=2011, album="", path='/static/mp3s/throwback/safesound.mp3', category="throwback"),
    Song(title="Coming Home", artist="Diddy", year=2010, album="", path='/static/mp3s/throwback/cominghome.mp3', category="throwback"),
    Song(title="Latch", artist="Disclosure", year=2013, album="", path='/static/mp3s/throwback/latch.mp3', category="throwback"),
    Song(title="Dog Days Are Over", artist="Florence + the Machine", year=2009, album="", path='/static/mp3s/throwback/dogdays.mp3', category="throwback"),
    Song(title="We Are Young", artist="Fun.", year=2011, album="", path='/static/mp3s/throwback/young.mp3', category="throwback"),
    Song(title="Replay", artist="Iyaz", year=2009, album="", path='/static/mp3s/throwback/replay.mp3', category="throwback"),
    Song(title="Mirrors", artist="Justin Timberlake", year=2013, album="", path='/static/mp3s/throwback/mirrors.mp3', category="throwback"),
    Song(title="Sex on Fire", artist="Kings Of Leon", year=2008, album="", path='/static/mp3s/throwback/sexonfire.mp3', category="throwback"),
    Song(title="Use Somebody", artist="Kings Of Leon", year=2008, album="", path='/static/mp3s/throwback/usesomebody.mp3', category="throwback"),
    Song(title="Little Lion Man", artist="Mumford And Sons", year=2009, album="", path='/static/mp3s/throwback/lionman.mp3', category="throwback"),
    Song(title="Animal", artist="Neon Trees", year=2010, album="", path='/static/mp3s/throwback/animal.mp3', category="throwback"),
    Song(title="Am I Wrong", artist="Nico & Vinz", year=2014, album="", path='/static/mp3s/throwback/amiwrong.mp3', category="throwback"),
    Song(title="Good Time", artist="Owl City", year=2012, album="", path='/static/mp3s/throwback/goodtime.mp3', category="throwback"),
    Song(title="Temperature", artist="Sean Paul", year=2005, album="", path='/static/mp3s/throwback/temperature.mp3', category="throwback"),
    Song(title="Meet Me Halfway", artist="The Black Eyed Peas", year=2009, album="", path='/static/mp3s/throwback/halfway.mp3', category="throwback"),
    Song(title="Apologize", artist="Timbaland", year=2007, album="", path='/static/mp3s/throwback/apologize.mp3', category="throwback"),

    ## rave mix ## (11)
    Song(title="Let's Go", artist="Calvin Harris", year=2012, album="", path='/static/mp3s/ravemix/letsgo.mp3', category="rave mix"),
    Song(title="I Need Your Love", artist="Calvin Harris", year=2013, album="", path='/static/mp3s/ravemix/yourlove.mp3', category="rave mix"),
    Song(title="You Make Me Feel...", artist="Cobra Starship", year=2011, album="", path='/static/mp3s/ravemix/makemefeel.mp3', category="rave mix"),
    Song(title="Wild Ones", artist="Flo Rida", year=2011, album="", path='/static/mp3s/ravemix/wildones.mp3', category="rave mix"),
    Song(title="I Love It", artist="Icona Pop", year=2012, album="", path='/static/mp3s/ravemix/iloveit.mp3', category="rave mix"),
    Song(title="I Took A Pill In Ibiza", artist="Mike Posner", year=2015, album="", path='/static/mp3s/ravemix/ibiza.mp3', category="rave mix"),
    Song(title="Sexy Bitch", artist="David Guetta", year=2009, album="", path='/static/mp3s/ravemix/sexybitch.mp3', category="rave mix"),
    Song(title="Where Them Girls At", artist="David Guetta", year=2011, album="", path='/static/mp3s/ravemix/girlsat.mp3', category="rave mix"),
    Song(title="Clarity", artist="Zedd", year=2012, album="", path='/static/mp3s/ravemix/clarity.mp3', category="rave mix"),
    Song(title="Stay The Night", artist="Zedd", year=2012, album="", path='/static/mp3s/ravemix/staynight.mp3', category="rave mix"),
    Song(title="Stay", artist="Zedd", year=2017, album="", path='/static/mp3s/ravemix/stay.mp3', category="rave mix"),

    ## late night drive ## (16)
    Song(title="3005", artist="Childish Gambino", year=2013, album="", path='/static/mp3s/latenightdrive/childish.mp3', category="late night drive"),
    Song(title="Don't", artist="Bryson Tiller", year=2015, album="", path='/static/mp3s/latenightdrive/dont.mp3', category="late night drive"),
    Song(title="Nights", artist="Frank Ocean", year=2016, album="", path='/static/mp3s/latenightdrive/nights.mp3', category="late night drive"),
    Song(title="In My Room", artist="Frank Ocean", year=2019, album="", path='/static/mp3s/latenightdrive/room.mp3', category="late night drive"),
    Song(title="Jungle", artist="Drake", year=2015, album="", path='/static/mp3s/latenightdrive/jungle.mp3', category="late night drive"),
    Song(title="Coaster", artist="Khalid", year=2017, album="", path='/static/mp3s/latenightdrive/coaster.mp3', category="late night drive"),
    Song(title="Look What You've Done", artist="Drake", year=2011, album="", path='/static/mp3s/latenightdrive/lookwhat.mp3', category="late night drive"),
    Song(title="2009", artist="Mac Miller", year=2018, album="", path='/static/mp3s/latenightdrive/twonine.mp3', category="late night drive"),
    Song(title="Self Care", artist="Mac Miller", year=2018, album="", path='/static/mp3s/latenightdrive/selfcare.mp3', category="late night drive"),
    Song(title="The Spins", artist="Mac Miller", year=2010, album="", path='/static/mp3s/latenightdrive/spins.mp3', category="late night drive"),
    Song(title="Sure Thing", artist="Miguel", year=2010, album="", path='/static/mp3s/latenightdrive/surething.mp3', category="late night drive"),
    Song(title="Pyramids", artist="Frank Ocean", year=2012, album="", path='/static/mp3s/latenightdrive/pyramids.mp3', category="late night drive"),
    Song(title="The Hills", artist="The Weeknd", year=2015, album="", path='/static/mp3s/latenightdrive/thehills.mp3', category="late night drive"),
    Song(title="The Color Violet", artist="Tory Lanez", year=2021, album="", path='/static/mp3s/latenightdrive/colorviolet.mp3', category="late night drive"),
    Song(title="Say It", artist="Tory Lanez", year=2016, album="", path='/static/mp3s/latenightdrive/sayit.mp3', category="late night drive"),
    Song(title="Violent Crimes", artist="Kanye West", year=2018, album="", path='/static/mp3s/latenightdrive/violent.mp3', category="late night drive"),

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
    categories = ["80s", "90s", "2000s", "dad rock", "girl pop", "opium", "rap caviar", "all"]
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

    avg_scores = {}

    for account in accounts:
        theirRounds = Round.objects.filter(player=account.username)

        sum_scores = sum(round.score for round in theirRounds)

        average_score = sum_scores / len(theirRounds) if theirRounds else 0

        avg_scores[account.username] = round(average_score, 2)

        # avg_scores.append({
        #     'username': account.username,
        #     'average': round(average_score, 2)
        # })
    
    sorted_accounts = sorted(accounts, key=lambda acc: -avg_scores.get(acc.username, 0))
    
    avgScores = [
        {'username': username, 'average': avg_scores[username]}
        for username in avg_scores
    ]
    
    # avgScores = sorted(avg_scores, key=lambda x: (-x['average']))
    

    return render(request, 'leaderboard.html', {
        'template_data': template_data,
        'accounts': sorted_accounts,
        'gameRound': newRound,
        'allRounds': allRounds,
        'username': username,
        'avg_scores': avgScores,
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


def add_round(request):
    if request.method == 'POST':
        username = request.session.get('username', '')

        if username != '':
            data = json.loads(request.body.decode('utf-8'))
            newScore = data.get('score', 0) 
            Round.objects.create(player=username, score=newScore)
            pdb.set_trace()
            return JsonResponse({'success': True, 'roundFor': username}, 200)
        else:
            return JsonResponse({'success': True}, 200)
    
    else:
        return JsonResponse({'success': False}, 400)

