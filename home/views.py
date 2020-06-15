from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

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

class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query',None)
        if not query:
            return redirect('/')

        self.view['search_query']=Item.objects.filter(title__icontains = query)
        return render(request,'search_product.html',self.view)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm Password']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'The username is already taken')
                return render(request, 'register.html')

            elif User.objects.filter(email=email).exists():
                messages.error(request,'The email is already registered')
                return render(request, 'register.html')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )

                user.save()
                messages.success(request, 'You are  registered')
                return render(request,'register.html')
        else:
            messages.success(request, 'The password does not match')
            return render(request, 'register.html')

    return render(request,'register.html')

def cart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        quantity = Cart.objects.get(slug =slug).quantity
        quantity = quantity+1
        Cart.objects.filter(slug=slug).update(quantity=quantity)
    else:
        username = request.user
        data = Cart.objects.create(
            user = username,
            slug = slug
        )
        data.save()
    return redirect('home:mycart')

def deletecart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        Cart.objects.filter(slug=slug).delete()
    return redirect('home:mycart')

def removecart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        quantity = Cart.objects.get(slug =slug).quantity
        quantity = quantity-1
        Cart.objects.filter(slug=slug).update(quantity=quantity)
    return redirect('home:mycart')


class CartView(BaseView):
   def get(self,request):
       self.view['slugs'] = Cart.objects.filter(checkout = False,user=request.user)
       # self.view['cart_items'] = Item.objects.all()
       return render(request, 'cart.html',self.view)
