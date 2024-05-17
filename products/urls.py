from django.urls import path
from .views import shop_detail, favorites, shop

urlpatterns = [
    path("detail/", shop_detail, name= 'shop_detail'),
    path("favorites/", favorites, name= 'favorites'),
    path('', shop , name= 'shop')
]
