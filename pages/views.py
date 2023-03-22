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
    # inside the {} is where you type in context. IE the context in whcih your html gets rendered
    # Meaning the HTML page creation is modular
    # returns the final HTML. 

def about_view(request,*args,**kwargs):
    my_context = {
        "my_text": "this is a context text",
        "my_number": 123,
        "my_list": [123,456,789],
        "this_is_true":True,
        "my_html": "<h1>In Built HTML</h1>"
    }
    return render(request,"about.html", my_context)


def contacts_page(request,*args, **kwargs):
    return render(request,"contacts.html", {} )