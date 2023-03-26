from django.db import models
from django.urls import reverse 

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)  # max_length = required
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2,max_digits = 10000)
    summary = models.TextField(blank=False,null = False)

    # This was created later in the database 
    # When you create a new field later on once your database is already in production
    # You will run into issues for previously logged in data. 
    # So you set a default value of True
    featured = models.BooleanField(default = False) # Options to put in are null = True, default = True


    # blank = True / False - Specify whether the field is supposed to be empty or not
    # default = XX --> default value if empty
    # null = xx --> can defined to be a null object or not


    # Dynamically returns products as the url no matter what you type in in the url.
    # This is for redirecting when you click on a link
    def get_absolute_url(self):
        # Or basically call this the function to redirect the url link 
        # return f"/product/{self.id}/"
        # print(reverse("product-detail",kwargs={"id":self.title}))
        return reverse("products:product-detail",kwargs={"my_id":self.id})
    