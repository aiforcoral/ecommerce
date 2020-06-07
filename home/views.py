from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import *

class BaseView(View):
    view = {}

class HomeView(BaseView):
    def get(self,request):
        # self.view['items'] = Item.objects.all()
        self.view['specil_items'] = Item.objects.filter(labels = 'special').reverse()[0:12]
        self.view['sliders']=Slider.objects.all()
        self.view['category']=Category.objects.all()
        self.view['subcategory'] = SubCategory.objects.all()
        self.view['add_one'] = Ad.objects.filter(rank=1)
        self.view['add_second'] = Ad.objects.filter(rank=2)
        self.view['add_third'] = Ad.objects.filter(rank=3)
        self.view['add_forth'] = Ad.objects.filter(rank=4)
        return render(self.request,'index.html',self.view)