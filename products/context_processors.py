from .models import favorite
from django.contrib.auth import get_user_model

user = get_user_model()


def favorite_count(request):
    if request.user.is_authenticated:
        return {'favorite_count': favorite.objects.filter(user=request.user).count()}
    return {'favorite_count': 0}