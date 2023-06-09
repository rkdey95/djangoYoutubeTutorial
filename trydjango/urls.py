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
from django.urls import path, include

# Import the respective views from the app folders
from pages.views import homepage_view
from pages.views import contacts_page
from pages.views import about_view

urlpatterns = [
    path('', homepage_view,name = "home"),
    path('admin/', admin.site.urls),
    path("home/",homepage_view,name = "homepage_view"),
    path("contacts/",contacts_page,name = "contacts_page"),
    path("about/",about_view,name = "about_page"),
    # Import urls for products specific
    path("products/",include("products.urls")),
    path("blog/",include("blog.urls")),
]
