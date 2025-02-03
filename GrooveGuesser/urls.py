from django.urls import path, include
from . import views

urlpatterns = [
    #grooveguesser test app
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
<<<<<<< HEAD
    path('game/', views.get_random_song, name='game')
=======
    path('user/', include('user.urls'))
>>>>>>> 99a5b76adb6e5ff93138413b71cb53b7707d6d31

    #user registration app
    # path('register',views.registerview, name="register"),




    #user login app


]