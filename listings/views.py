from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404

from .models import Listing


def index(request):
    # 1 -----------------------------------------
    listings = Listing.objects.all()
    # 2 -----------------------------------------
    # listings = Listing.objects.order_by('-list_date')
    # 3 -----------------------------------------
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return HttpResponse('<h1>Listings</h1>')
