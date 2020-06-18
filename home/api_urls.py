from rest_framework import routers

from home.views import  ItemViewSet,CategoryViewSet,SubCategoryViewSet,ItemFilterListView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('items',ItemViewSet)
router.register('category',CategoryViewSet)
router.register('subcategory',SubCategoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('filteritem/',ItemFilterListView.as_view(),name='filteritem'),
]