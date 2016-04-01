from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from config import CONFIG
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
                print result.user
                if result.provider.name == 'tw':
                    response.write('Your are logged in with Twitter.<br />')
                     # We will get the user's 5 most recent tweets.
                    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
                    # You can pass a dictionary of querystring parameters.
                    access_response = result.provider.access(url, {'count': 5})
                    if access_response.status == 200:
                        if type(access_response.data) is list:
                            # Twitter returns the tweets as a JSON list.
                            response.write('Your 5 most recent tweets:')
                            for tweet in access_response.data:
                                text = tweet.get('text')
                                date = tweet.get('created_at')
                                
                                response.write(u'<h3>{0}</h3>'.format(text))
                                response.write(u'Tweeted on: {0}'.format(date))
                                
                    elif response.data.get('errors'):
                        response.write(u'Damn that error: {0}!'.\
                                            format(response.data.get('errors')))
                    else:
                        response.write('Damn that unknown error!<br />')
                        response.write(u'Status: {0}'.format(response.status))
    return response
  

# def twitter_authenticated(request):
#     print id(request)
#     print(request.session.keys())

#     token = oauth.Token(request.session['request_token']['oauth_token'],
#         request.session['request_token']['oauth_token_secret'])
#     # Use request token to build a new client
    
#     token.set_token(request.GET['oauth_token'])
#     token.set_verifier(request.GET['oauth_verifier'])
#     client = oauth.Client(consumer, token)
#     # Request the authorized access token from Twitter
#     resp, content = client.request(access_token_url, "GET")
#     # if resp['status'] != '200':
#     #     raise Exception("Invalid response from Twitter.")
#     access_token = dict(cgi.parse_qsl(content))
#     print ("*")*60, "Access_token:", access_token

    # # Lookup user or create if not exists.
    # try:
    #     user = User.objects.get(username=access_token['screen_name'])
    #     print "User: ", user
    # except User.DoesNotExist:
    #     user = User.objects.create_user(access_token['screen_name'], '%s@twitter.com' % access_token['screen_name'], access_token['oauth_token_secret'])

    #     profile = Profile()
    #     profile.user = user
    #     profile.oauth_token = access_token['oauth_token']
    #     profile.oauth_secret = access_token['oauth_token_secret']
    #     profile.save()

    # user = authenticate(username=access_token['screen_name'], password=access_token['oauth_token_secret'])
    # login(request, user)
    # return HttpResponseRedirect('/home')

# @login_required(login_url='/')
def home(request):
    return render(request, 'logreg/home.html')

# @login_required(login_url='/')
def twitter_logout(request):
    logout(request)
    return redirect('/')


