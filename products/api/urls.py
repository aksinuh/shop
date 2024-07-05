from django.urls import path
from .views import categorys,products

urlpatterns = [
    path('categorys',categorys, name="categorys_api_list"),
    path('products',products, name="praducts_api_list")
]
