from django.shortcuts import render

# Create your views here.
from django.views.generic import View, DetailView
from .models import *

class BaseView(View):
    view = {}

class HomeView(BaseView):
    def get(self,request):
        self.view['items'] = Item.objects.all()
        self.view['specil_items'] = Item.objects.filter(labels = 'special').reverse()[0:12]
        self.view['sliders']=Slider.objects.all()
        self.view['category']=Category.objects.all()
        self.view['subcategory'] = SubCategory.objects.all()
        self.view['add_one'] = Ad.objects.filter(rank=1)
        self.view['add_second'] = Ad.objects.filter(rank=2)
        self.view['add_third'] = Ad.objects.filter(rank=3)
        self.view['add_forth'] = Ad.objects.filter(rank=4)
        self.view['special_subcat'] = SubCategory.objects.filter(labels = 'special')
        return render(self.request,'index.html',self.view)

class ItemDetailView(DetailView):
    model=Item
    template_name = 'single.html'

class Subcategory(BaseView):
    def get(self,request,id):
        self.view['subcat_items'] = Item.objects.filter(subcategory_id = id)

        return render(self.request, 'kitchen.html', self.view)