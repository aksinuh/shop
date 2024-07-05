from django.urls import path
from .views import CantactCreateView
urlpatterns = [
    path('cantact/', CantactCreateView.as_view() , name= 'cantact'),
    
]
