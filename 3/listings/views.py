from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# ! 1 -----------------------------------------
def index(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return HttpResponse('<h1>Listings</h1>')
