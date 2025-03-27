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
<<<<<<< HEAD
    
    # NEW ADDITION
    path('signup/', views.signup, name='signup'),

=======
    path('logout', views.logout, name='logout')
>>>>>>> 5d60d617e38ce0c1c9edf3d8edd1632b89c8e69a


    #user login app
]
