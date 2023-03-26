from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse     # Library to enable HTTP 
from.models import Product
from .forms import ProductForm,RawProductForm

# Create your views here.

# # Changes the view or the look of the webpage
# def homepage_view(*args, **kwargs):
#     return HttpResponse("<h1>Hello  World</h1>")        # Return a HTML code 

# def contacts_page(*args, **kwargs):
#     return HttpResponse("<h1>Hello  World</h1>")
#%%
def product_list_view(request):
    # Returns a list of all the objects 
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,"products/product_list.html",context)


#%%
def product_delete_view(request,my_id): 
    obj = get_object_or_404(Product,id=my_id)
    if request.method == "POST":
        # Confirming a delete from a POST request. 
        obj.delete()
        return redirect("../../")
    context = {
        "object":obj
    }
    return render(request,"products/product_delete.html",context)

#%%
# Want to view HTML based on product ID
# Dyanmic HTML page routing
def dynamic_lookup_view(request,my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product,id=my_id) 
    
    # try: 
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist: 
    #     raise Http404

    context = {
        "object":obj        }
    return render(request, "products/product_detail.html",context)

#%%
def product_create_view(request):
    initial_data = {
        "title": "This is my awesome title"
    }
    # Load a data from DB and pass to the form to view

    # Pass in an instance if you want to make modifications to an object id 
    # If you don want to make modifications then this is not needed. 
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, initial = initial_data, instance = obj)
    if form.is_valid():
        form.save()
        # Rerender an empty form once you save it
        form = ProductForm()
    context = {
        "form":form
        }
    return render(request, "products/product_create.html",context)

# def product_create_view(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#     context = {}
#     # Get the title of the POST request
    
#     return render(request, "products/product_create.html",context)

# def product_create_view(request):
#     # Initilize form by default for get method. 
#     # This is to refresh the page by default.
#     myform =  RawProductForm()
    
#     # If request is POST then pass the data from POST
#     if request.method == "POST":
#         # Pass the form into context. Then send the form instance to context
#         # request.POST here passes the data from form to backend 
#         myform = RawProductForm(request.POST)
#         if myform.is_valid():
#             # Now the data is good to save
#             print(myform.cleaned_data)
#             Product.objects.create(**myform.cleaned_data)
#         else: 
#             print(myform.errors)
#     context = {
#         "form": myform
#     }
#     # Get the title of the POST request
#     return render(request, "products/product_create.html",context)

#%%
def product_detail_view(request):
    # Get the Product Object of id=1 from the database
    obj = Product.objects.get(id=3)
    # context = {
    #     "title": obj.title,
    #     "price": obj.price,
    #     "description": obj.description
    # }

    # Pass the object itself and then deal with it inside HTML later on
    # This makes things more modular if you make any changes to the structure of the product class later on
    context = {"object":obj}
    return render(request, "products/product_detail.html",context)

# Hierrachy of data being read
# 1. Template folder which you specify in settings (higher priority)
# 2. Template folder within the app / object itself ie. within products itself. 
# If both have the same name then it takes from the master template folder not the object template folder itself





