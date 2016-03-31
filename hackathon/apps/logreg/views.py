from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from models import Profile
from ..hackathon import config.py

def index(request):
    return render('index.html')

@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')

@login_required
def twitter_logout(request):
    auth_logout(request)
    return redirect('/')
