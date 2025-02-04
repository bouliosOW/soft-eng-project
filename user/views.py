from django.shortcuts import render

def users(request):
    return render(request, 'user/users.html')

def login(request):
    return render(request, 'user/login.html')