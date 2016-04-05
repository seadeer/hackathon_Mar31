from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from config import CONFIG
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Profile
import oauth2 as oauth
import cgi

# Twitter token and secret for the app
authomatic = Authomatic(CONFIG, 'mysupersecretsecret')

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authenticate_url = "https://api.twitter.com/oauth/authorize"

def index(request):
    return render(request, 'logreg/index.html')

def twitter_authenticated(request):
    response = HttpResponse()
    result = authomatic.login(DjangoAdapter(request, response), 'tw')
    if result:
        response.write('<a href="..">Home</a>')
        if result.error:
            response.write("<h2>Oops, we've got an error: {0}</h2>".format(result.error.message))
        elif result.user:
            if not (result.user.name and result.user.id):
                result.user.update()
            response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
            response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
            response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))

            if result.user.credentials:
                credentials = result.user.credentials
                print credentials
                twusername = result.user.username
                print twusername
                if result.provider.name == 'tw':
                    response.write('Your are logged in with Twitter.<br />')
                     # We will get the user's 5 most recent tweets.
                    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
                    # You can pass a dictionary of querystring parameters.
                    access_response = result.provider.access(url, {'count': 5})
                    
                    if access_response.status == 200:
                        try:
                            user = User.objects.get(username=twusername)
                            request.session['id'] = user.id
                            print "User exists!", user
                        except User.DoesNotExist:
                            token = result.user.credentials.token
                            token_secret = result.user.credentials.token_secret
                            user = User.objects.create_user(twusername, '%s@twitter.com' % twusername, token_secret)
                            profile = Profile()
                            profile.user = user
                            profile.oauth_token = token
                            profile.oauth_secret = token_secret
                            profile.save()
                            user = User.objects.get(username=twusername) 
                            request.session['id'] = user.id
                            pass

                        # if type(access_response.data) is list:
                        #     # Twitter returns the tweets as a JSON list.
                        #     response.write('Your 5 most recent tweets:')
                        #     for tweet in access_response.data:
                        #         text = tweet.get('text')
                        #         date = tweet.get('created_at')
                                
                        #         response.write(u'<h3>{0}</h3>'.format(text))
                        #         response.write(u'Tweeted on: {0}'.format(date))
                        request.session['login'] = 'twitter'
                        return HttpResponseRedirect('/home')                                
                    elif response.data.get('errors'):
                        response.write(u'Damn that error: {0}!'.\
                                            format(response.data.get('errors')))
                    else:
                        response.write('Damn that unknown error!<br />')
                        response.write(u'Status: {0}'.format(response.status))
    return response
  
def createUser(request):
    user = User.objects.create(first_name=request.POST['first_name'], username=request.POST['username'],\
        email=request.POST['email'], password=request.POST['password'])
    print user.id
    request.session['id'] = user.id
    return redirect('home')

def login(request):
    print request.POST['username']
    user = User.objects.get(username=request.POST['username'])
    request.session['id'] = user.id
    print User.objects.get(username=request.POST['username'])
    request.session['login'] = 'app'
    return redirect('home')

def home(request):
    user = User.objects.get(id=request.session['id'])
    stuff = {
        'login_meth': request.session['login'],
        'user': user,
    }
    return render(request, 'logreg/home.html', stuff)

def logout(request):
    del request.session['id']
    return redirect('index')

def twitter_logout(request):
    logout(request)
    return redirect('index')


