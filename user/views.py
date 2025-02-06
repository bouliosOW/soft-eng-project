import random
import os
from django.shortcuts import render, redirect
import requests
import json
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from . import forms
from .models import Account



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
    
    return render(request, 'user/login.html', {
        'template_data': template_data
    })

def get_new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # UPDATE DATABASE HERE
            Account.objects.create(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
            return redirect('/login')
    
    else: 
        form = SignUpForm()

    return render(request, 'users.html', {'form': form})

def log_into_account(request):
    pass

def seeAccounts(request):
    accounts = Account.objects.all
    return render(request, "user/login.html", {
        'accounts': accounts
    })