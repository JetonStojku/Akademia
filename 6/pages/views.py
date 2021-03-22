from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)


def test_1(request):

    furrat_bukes = {'furrat': [
        {'name': 'Furra 1', 'months': [
            {'month': 'Janar', 'sales': [500, 600, 800, 7000, 1000]},
            {'month': 'Shkurt', 'sales': [5000, 6000, 8000, 700, 100]},
            {'month': 'Mars', 'sales': [700, 600, 400, 3000, 2000]},
        ]},

        {'name': 'Furra 2', 'months': [
            {'month': 'Janar', 'sales': [500, 600, 800, 7000, 1000]},
            {'month': 'Shkurt', 'sales': [500, 6000, 800, 700, 100]},
            {'month': 'Mars', 'sales': [700, 600, 400, 3000, 2000]},
        ]},

        {'name': 'Furra 3', 'months': [
            {'month': 'Janar', 'sales': [500, 600, 800, 7000, 1000]},
            {'month': 'Shkurt', 'sales': [5000, 6000, 800, 700, 100]},
            {'month': 'Mars', 'sales': [700, 600, 40, 3000, 2000]},
        ]},

    ]}

    return render(request, 'pages/test_1.html', furrat_bukes)



    # frr = [a, b, c]
    #
    # a = {
    #     'name': 'f1',
    #     'months': [m1, m2, m3]
    # }
    #
    # m1 = {
    #     'month': 'janar',
    #     'sales': [500, 600, 700]
    # }

