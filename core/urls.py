from django.urls import path
from .views import contact
urlpatterns = [
    path('home/', contact , name= 'cantact'),
    
]
