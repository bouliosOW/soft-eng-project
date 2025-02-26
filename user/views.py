import random
import os
from django.shortcuts import render, redirect
import requests
import json
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from . import forms
from .models import Account


'''
    IMPORTANT ---------------------------------------------------------
    This code
        Account.objects.create(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
    creates a new object within the table

    This code
        newRound = Round(player="newplayer", score=1)
    creates a temporary object that does not last beyond this instance of the page
'''



def users(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    form = forms.SignUpForm()
    return render(request, 'user/users.html', {
        'template_data': template_data,
        'form': form
    })

def login(request):
    template_data = {}
    template_data['title'] = 'Log In'
    accounts = Account.objects.all()
    form = forms.LoginForm()
    return render(request, 'user/login.html', {
        'template_data': template_data,
        'accounts': accounts,
        'form': form
    })

# The form isn't working to create new Account records. Must fix

def get_new_user(request):
    #print("Arrived:", "at view get_new_user")
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            #print("crash:", "out")
            # UPDATE DATABASE HERE
            Account.objects.create(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
            return redirect('user.login')
        else:
            print("Form errors:", form.errors) 
            return redirect('user.signup')  
    


    
    return render(request, 'users.html', {'form': form})


def userHome(request):
    username = request.session.get('username')
    # password = request.session.get('password')
    accounts = Account.objects.all()
    return render(request, 'user/userHome.html', {'username': username, 'accounts': accounts})


def user_enter(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            account = Account.objects.filter(username= form.cleaned_data["username"], password = form.cleaned_data["password"])
            
            if account:
                # username = request.POST.get('username')
                # password = request.POST.get('password')

                # request.session['account'] = account
                request.session['username'] = form.cleaned_data["username"]

                # account_data = list(account.values())
                # request.session['account'] = account_data

                return redirect('user.userHome')
        
        else:
            print("Form errors:", form.errors)
            return redirect('user.login')
    
    return render(request, 'login.html', {'form': form})


