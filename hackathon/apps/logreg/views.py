from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.models import User
from django.contrib.auth.decorators import login_required
from models import Profile
import config
import cgi

# Twitter token and secret for the app
consumer = oauth.Consumer(config.TWITTER_KEY, config.TWITTER_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authenticate_url = "https://api.twitter.com/oauth/authenticate"

def index(request):
    return render(request, 'logreg/index.html')

def login_twitter(request):
    # Get token from Twitter
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter")

    # Store the token in session
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Redirect user to authentication URL
    url = "%s?oauth_token=%s" %(authenticate_url, request.session['request_token']['oauth_token'])

    return HttpResponseRedirect('/home')

@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')

@login_required
def logout_twitter(request):
    auth_logout(request)
    return redirect('/')
