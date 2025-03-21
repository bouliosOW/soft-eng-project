from django.urls import path, include
from . import views

urlpatterns = [
    #grooveguesser test app
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('game/', views.game, name='game'),
    path('user/', include('user.urls')),
    path('leaderboard', views.leaderboard, name="leaderboard"),
    #user registration app
    # path('register',views.registerview, name="register"),

    path('pregame', views.pregame, name='pregame'),
    path('logout', views.logout, name='logout')


    #user login app
]
