from django.urls import path
from . import views

urlpatterns = [
    #grooveguesser test app
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('game/', views.get_random_song, name='game')

    #user registration app
    # path('register',views.registerview, name="register"),




    #user login app


]