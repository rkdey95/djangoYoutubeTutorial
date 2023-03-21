from django.shortcuts import render
from django.http import HttpResponse     # Library to enable HTTP 

# Create your views here.

# Changes the view or the look of the webpage
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>Hello  World</h1>")        # Return a HTML code 

def contacts_page(*args, **kwargs):
    return HttpResponse("<h1>Hello  World</h1>")


