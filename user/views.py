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
    accounts = Account.objects.all()
    return render(request, 'user/login.html', {
        'template_data': template_data,
        'accounts': accounts
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
            print("Form errors:", form.errors)  # Debugging
            return redirect('user.signup')  # Redirect back on failure
    
    # else: 
    #     #print("super:", "Crash out")
    #     form = SignUpForm()

    
    return render(request, 'users.html', {'form': form})


