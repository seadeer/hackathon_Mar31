from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Listing, Message

def new(request):
	return render(request, 'findpad/new.html')

def create(request):
	aUser = User.objects.get(id=request.session['id'])
	print request.POST
	print request.POST['address']
	try:
		request.POST['pets']
	except:
		pets = False
	else:
		pets = True
	try:
		request.POST['washer']
	except:
		washer = False
	else:
		washer = True
	Listing.objects.create(address=request.POST['address'], \
						   lister=aUser,\
						   description=request.POST['description'], \
						   bedrooms=request.POST['bedrooms'],\
						   rent=request.POST['rent'],\
						   isAvailable=True,\
						   pets=pets,\
						   washer=washer,\
						   created_at=timezone.now())
	return redirect('show')

def show(request):
	listings = Listing.objects.all()
	stuff = {
		'listings': listings
	}
	print stuff
	return render(request, 'findpad/listings.html', stuff)

def showOne(request, listing):
	thisListing = Listing.objects.get(id=listing)
	stuff = {
		'listing': thisListing
	}
	print stuff
	return render(request, 'findpad/show.html', stuff)

def send(request, lister):
	sender = User.objects.get(id=request.session['id'])
	recipient = Listing.objects.get(lister=lister)
	Message.objects.create(content=request.POST['content'], sender=sender, \
		recipient=recipient, created_at=timezone.now())
	return redirect('show')
