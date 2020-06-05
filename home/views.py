from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import *

class BaseView(View):
    view = {}

class HomeView(BaseView):
    def get(self,request):
        self.view['items'] = Item.objects.all()
        self.view['sliders']=Slider.objects.all()
        self.view['category']=Category.objects.all()
        self.view['subcategory'] = SubCategory.objects.all()
        return render(self.request,'index.html',self.view)