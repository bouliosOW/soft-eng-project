from django.urls import path, include
from . import views

urlpatterns = [
    #grooveguesser test app
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('game/', views.get_random_song, name='game'),
<<<<<<< HEAD
    path('user/', include('user.urls')),
=======
    path('user/', include('user.urls'))
>>>>>>> 4c93e09338a89e1d7d6d9caed424d309c87640ca

    #user registration app
    # path('register',views.registerview, name="register"),




    #user login app
<<<<<<< HEAD

]
=======
]
>>>>>>> 4c93e09338a89e1d7d6d9caed424d309c87640ca
