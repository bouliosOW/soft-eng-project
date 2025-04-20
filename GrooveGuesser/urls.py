from django.urls import path, include
from . import views

urlpatterns = [
    #grooveguesser test app
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('game/', views.game, name='game'),
    path('user/', include('user.urls')),
    path('audio-player/', views.audio_player, name='audio-player'),
    path('leaderboard', views.leaderboard, name="leaderboard"),

    path('leaderboard', views.leaderboard, name="leaderboard"),
    #user registration app
    # path('register',views.registerview, name="register"),

    path('pregame', views.pregame, name='pregame'),
    
    # NEW ADDITION
    path('signup/', views.signup, name='signup'),

    path('logout', views.logout, name='logout'),
    
    #NEW ADD
    path('login', views.logout, name='login'),

    path('add_round', views.add_round, name='add_round')


    #user login app

]
