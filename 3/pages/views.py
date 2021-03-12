from django.shortcuts import render
from django.http import HttpResponse

# ! 1 -----------------------------------------
# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')
#
# def about(request):
#     return HttpResponse('<h1>About</h1>')


# ! 2 -----------------------------------------
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
