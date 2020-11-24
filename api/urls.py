from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet
from .views import  ListCategory, DetailCategory, ListProduct, DetailProduct


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
]