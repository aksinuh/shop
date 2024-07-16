from django.urls import path
from .views import categorys,products_update,praductListAPIView,praductRetrieveUpdateDestroyAPIView,productCreateAPIView

urlpatterns = [
    path('categorys',categorys, name="categorys_api_list"),
    path('products',praductListAPIView.as_view(), name="praducts_api_list"),
    path('producthome',productCreateAPIView.as_view(), name="praducts_api_create"),
    path('product/<int:pk>',praductRetrieveUpdateDestroyAPIView.as_view(), name="praducts_api_update")
]
