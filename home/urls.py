from .views import homeview
from django.urls import path
app_name = 'home'


urlpatterns = [
    path('', homeview,name='home'),

]
