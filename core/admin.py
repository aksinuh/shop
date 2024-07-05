from django.contrib import admin
from .models import ContactUs
# Register your models here.

@admin.register(ContactUs)
class ContactUsadmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "subject"]
    list_display_links = ["name"]