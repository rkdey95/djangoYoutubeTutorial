from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)  # max_length = required
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2,max_digits = 10000)
    summary = models.TextField()

    # This was created later in the database 
    # When you create a new field later on once your database is already in production
    # You will run into issues for previously logged in data. 
    # So you set a default value of True
    featured = models.BooleanField(default = True) # Options to put in are null = True, default = True


    # blank = True / False - Specify whether the field is supposed to be empty or not
    # default = XX --> default value if empty
    # null = xx --> can defined to be a null object or not