from django.contrib import admin
from .models import (
    product, detail, category, discount, images,
    color, size, TimeStamp, comment, favorite,
)

# Register your models here.

admin.site.register(TimeStamp)


@admin.register(detail)
class detailadmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "product", "color", "size", "discounted_price"]
    list_display_links = ["title"]
    list_editable = ["color", "size"]


@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display = ["id", "title", "category"]
    list_display_links = ["title"]
    list_editable = ["category"]
    

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
@admin.register(color)
class coloradmin(admin.ModelAdmin):
    list_display = ["id", "color"]
    
    
@admin.register(discount)
class discountadmin(admin.ModelAdmin):
    list_display = ["id", "rate"]
    
    
@admin.register(images)
class imagesadmin(admin.ModelAdmin):
    list_display = ["id", "product"]
    
    
@admin.register(size)
class sizeadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    
    
@admin.register(comment)
class commentadmin(admin.ModelAdmin):
    list_display = ["id", "product", "body", "user"]
    
    
@admin.register(favorite)
class favoriteadmin(admin.ModelAdmin):
    list_display = ["id", "user"]