from django.urls import path
from .views import favorites
from django.conf import settings
from django.conf.urls.static import static
from .views import ShopListView,ShopDetailView

urlpatterns = [
    path("detail/<int:pk>", ShopDetailView.as_view(), name= 'shop_detail'),
    path("favorites/", favorites, name= 'favorites'),
    path('', ShopListView.as_view(), name= 'shop')
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)