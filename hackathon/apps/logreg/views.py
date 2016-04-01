from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
# Create your views here.
def index(request):
	return render(request, 'logreg/index.html')

def createUser(request):
	user = User.objects.create(name=request.POST['name'], username=request.POST['username'],\
		email=request.POST['email'], password=request.POST['password'], created_at=timezone.now())
	print user.id
	request.session['id'] = user.id
	return redirect('home')

def login(request):
	print request.POST['username']
	user = User.objects.get(username=request.POST['username'])
	request.session['id'] = user.id
	print 
	print User.objects.get(username=request.POST['username'])
	return redirect('home')

def logout(request):
	del request.session['id']
	return redirect('index')

def home(request):
	user = User.objects.get(id=request.session['id'])
	stuff = {
		'user': user.username
	}
	return render(request, 'logreg/home.html', stuff)