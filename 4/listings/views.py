from django.http import HttpResponse
from django.shortcuts import render

from .models import Listing


# ! 1 -----------------------------------------
def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


# def listing(request, listing_id):
def listing(request):
    return HttpResponse('<h1>Listings</h1>')


def search(request):
    return HttpResponse('<h1>Listings</h1>')
