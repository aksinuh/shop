from django.urls import path
from .views import favorites
from django.conf import settings
from django.conf.urls.static import static
from .views import ShopDetailView, add_to_favorites, remove_favorite, favorites, ShopListView


urlpatterns = [
    path("detail/<slug:slug>", ShopDetailView.as_view(), name='shop_detail'),
    path('favorites/', favorites, name='favorites'),
    path('favorites/add/<int:id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:id>/', remove_favorite, name='remove_favorite'),
    path('', ShopListView.as_view(), name='shop'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




