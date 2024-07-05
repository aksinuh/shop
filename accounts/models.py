from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    photo_profil = models.ImageField(upload_to= "user_profil" , null= True , blank= True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = None
    last_name = None
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def get_avatar(self):
        if self.photo_profil:
            return self.photo_profil.url
        else:
            return "/static/img/profil_admin.png"
