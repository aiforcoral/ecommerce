from django.contrib.auth.models import User
from .models import Slider,Item,Category,SubCategory,Ad,Contact
from rest_framework import serializers

class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['title','description','slug','image']

class SubCategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['title','description','slug','image','labels','category','status']


class ItemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['title','slug','price','discounted_price','status','stock','image','category','subcategory']