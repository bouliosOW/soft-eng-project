from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users, name="user.signup"),
    path("login", views.login, name="user.login"),
    # path('about', include('grooveguesser.urls')),
    # This is causing errors, some kind of infinite loop relating to the routes?
    # it may be difficult to have the navbar work 2 ways, will focus on forms first
    path("process", views.get_new_user, name="user.get_new_user"),
    path("userHome", views.userHome, name="user.userHome"),
    path("enter", views.user_enter, name="user.user_enter"),
]