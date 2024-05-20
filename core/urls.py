from django.urls import path
from .views import contact
urlpatterns = [
    path('cantact/', contact , name= 'cantact'),
    
]
