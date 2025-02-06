from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users),
    path("login", views.login, name="user.login"),
    # path('about', include('grooveguesser.urls')),
    # This is causing errors, some kind of infinite loop relating to the routes?
    # it may be difficult to have the navbar work 2 ways, will focus on forms first

]