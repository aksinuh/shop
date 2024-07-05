from django.db import models
from .validators import validate_gmail

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=(validate_gmail,))
    subject = models.CharField(max_length= 150)
    message = models.TextField()
    
    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "cantacts"
    
    def __str__(self) -> str:
        return self.name