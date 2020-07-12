from django.conf import settings
from django.db import models
from django.urls import reverse

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
    def get_subcat_url(self):
        return reverse("home:subcategory",kwargs={'id':self.id})



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
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    def get_item_url(self):
        return reverse("home:product",kwargs={'slug':self.slug})
    def add_to_cat(self):
        return reverse("home:cart", kwargs={'slug': self.slug})

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

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    # items = models.ForeignKey(Item, on_delete=models.CASCADE, default =1)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def remove_one_item(self):
        return reverse("home:remove-one-item", kwargs={'slug': self.slug})

    def remove_all_item(self):
        return reverse("home:remove-all-item", kwargs={'slug': self.slug})

