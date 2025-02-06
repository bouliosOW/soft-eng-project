import random
import os
from django.shortcuts import render
import requests
import json




def users(request):
    return render(request, 'user/users.html')

def login(request):
    return render(request, 'user/login.html')