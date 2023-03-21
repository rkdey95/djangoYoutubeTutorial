from django.shortcuts import render
from django.http import HttpResponse     # Library to enable HTTP 

# Create your views here.

# Changes the view or the look of the webpage
def homepage_view(request, *args, **kwargs):
    # The inputs into the HTTP request function is the request itself and other miscellaneous inputs as and when required. 
    print(request.user)     # Get the user request
    print(args,kwargs)
    
    # return HttpResponse("<h1>Hello  World</h1>")        # Return a HTML code manually written
    return render(request,"home.html", {} ) # use the render fucntion to manually return a html template 


def contacts_page(request,*args, **kwargs):
    return render(request,"contacts.html", {} )