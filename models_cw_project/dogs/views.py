

# importing response function

from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.


# index server page response
def index(request):
        return HttpResponse("Hello, world")