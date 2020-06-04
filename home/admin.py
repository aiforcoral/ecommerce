from django.contrib import admin
from .models import Item,Contact,Category,SubCategory,Slider,Ad
# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Contact)