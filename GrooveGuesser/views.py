from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("Hello, you're accessing the GrooveGuesser app.")

def about(request):
    return HttpResponse("GrooveGuesser is a song guessing game.")

