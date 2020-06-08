from django.db import models
STATUS = (('active','Active'),('inactive','Inactive'),('','Default'))
STOCK = (('In Stock','In Stock'),('Out Of Stock','Out Of Stock'))
LABELS = (('special','special'),('','Non Special'))
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    slug = models.CharField(max_length=500,unique=True)
    image = models.TextField()

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    slug = models.CharField(max_length=500, unique=True)
    image = models.TextField()
    labels = models.CharField(max_length=300,choices=LABELS,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=200,choices=STATUS,blank=True )
    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=400)
    slug = models.CharField(max_length=500,default='product')
    price = models.IntegerField()
    discounted_price = models.IntegerField(blank = True)
    status = models.CharField(max_length=50,choices=STATUS,blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    stock = models.CharField(max_length=50,choices=STOCK)
    labels = models.CharField(max_length=300, choices=LABELS,blank=True)
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=300)
    image = models.TextField()
    rank = models.IntegerField()
    description = models.TextField(blank = True)
    status = models.CharField(max_length=50,choices=STATUS,blank=True)

    def __str__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length=400)
    image = models.TextField()
    rank = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=300)
    message = models.TextField()
    contact_id = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.email