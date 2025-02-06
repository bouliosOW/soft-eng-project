import random
import os
from django.shortcuts import render
import requests
import json
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from . import forms



def users(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    return render(request, 'user/users.html', {
        'template_data': template_data
    })

def login(request):
    template_data = {}
    template_data['title'] = 'Log In'
    form = forms.SignUpForm()
    return render(request, 'user/login.html', { form: form }, {
        'template_data': template_data
    })

def get_new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # UPDATE DATABASE HERE
            return HttpResponseRedirect('login')
    
    else:
        form = SignUpForm()
    
    return render(request, 'users.html', {'form': form})