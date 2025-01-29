from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm #registration (WIP PF)
from django.http import HttpResponse,JsonResponse

#grooveguesser test responses
def index(request):
    # return HttpResponse("Hello, Welcome to the GrooveGuesser app.") (WIP PF)
    return render(request, 'GrooveGuesser.html')

def about(request):
    # return HttpResponse("GrooveGuesser is a song guessing game.") (WIP PF)
    return render(request, 'about.html')





#registration app (WIP PF)
# def registerview(request):
#     form = UserCreationForm()
#     return render(request, "users/registers.html", { "form": form })