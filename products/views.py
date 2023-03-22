from django.shortcuts import render
from django.http import HttpResponse     # Library to enable HTTP 
from.models import Product

# Create your views here.

# # Changes the view or the look of the webpage
# def homepage_view(*args, **kwargs):
#     return HttpResponse("<h1>Hello  World</h1>")        # Return a HTML code 

# def contacts_page(*args, **kwargs):
#     return HttpResponse("<h1>Hello  World</h1>")

def product_detail_view(request):
    # Get the Product Object of id=1 from the database
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "price": obj.price,
    #     "description": obj.description
    # }

    # Pass the object itself and then deal with it inside HTML later on
    # This makes things more modular if you make any changes to the structure of the product class later on
    context = {"object":obj}
    return render(request, "product/detail.html",context)
