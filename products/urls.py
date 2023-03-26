"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Import the respective views from the app folders
from pages.views import homepage_view
from pages.views import contacts_page
from pages.views import about_view
from products.views import product_detail_view
from products.views import product_create_view
from products.views import dynamic_lookup_view
from products.views import product_delete_view
from products.views import product_list_view

# Namespacing meaning to tell that this fellas name is "products"
app_name = 'products'
urlpatterns = [
    path("create/",product_create_view,name = "product_create_page"),
    path("",product_detail_view,name = "product_page"),
    path("<int:my_id>/",dynamic_lookup_view,name ="product-detail"),
    path("<int:my_id>/delete/",product_delete_view, name = 'product-delete'),
    path("productView",product_list_view,name="product-list")
]
