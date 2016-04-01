from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
import oauth2 as oauth
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

def twitter_login(request):
    # Get token from Twitter
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter")

    # Store the token in session
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Redirect user to authentication URL
    url = "%s?oauth_token=%s" %(authenticate_url, request.session['request_token']['oauth_token'])
    return HttpResponseRedirect(url)

def twitter_authenticated(request):
    # Use request token to build a new client
    token = oauth.Token(request.session['request_token']['oauth_token'], request.session['request_token']['oauth_token_secret'])
    token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)
    return render_to_response('logreg/home.html')

    # Request the authorized access token from Twitter
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response from Twitter.")
    access_token = dict(cgi.parse_qsl(content))

    # Lookup user or create if not exists.
    try:
        user = User.objects.get(username=access_token['screen_name'])
    except User.DoesNotExist:
        user = User.objects.create_user(access_token['screen_name'], '%s@twitter.com' % access_token['screen_name'], access_token['oauth_token_secret'])

        profile = Profile()
        profile.user = user
        profile.oauth_token = access_token['oauth_token']
        profile.oauth_secret = access_token['oauth_token_secret']
        profile.save()

    user = authenticate(username=access_token['screen_name'], password=access_token['oauth_token_secret'])
    login(request, user)
    return redirect('/home')

# @login_required()
def home(request):
    return render(request, 'logreg/home.html')

# @login_required
def twitter_logout(request):
    logout(request)
    return redirect('/')

