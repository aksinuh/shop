from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal
from django.urls import reverse_lazy
# Create your models here.

User = get_user_model()

class product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey("category",on_delete= models.CASCADE, null= True, blank=True)
    image = models.ImageField(upload_to="shop_image/", null= True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    
class discount(models.Model):
    rate = models.IntegerField()
    
    
class detail(models.Model):
    title = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    product = models.ForeignKey(product, on_delete= models.CASCADE)
    discount = models.ForeignKey(discount, on_delete=models.CASCADE, null=True, blank=True)
    properties = models.TextField()
    image = models.ImageField(upload_to="product_img")
    color = models.ForeignKey("color",on_delete=models.CASCADE, related_name="produc",null=True,blank=True)
    size = models.ForeignKey("size", on_delete=models.CASCADE, related_name="products",null=True,blank=True)
    display = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    
    def discounted_price(self):
        if self.discount:
            discount_rate = Decimal(self.discount.rate) / Decimal(100)
            return round(self.price * (1 - discount_rate),2)
        return self.price

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse_lazy("shop_detail", kwargs={"slug": self.slug})
    

class category(models.Model):
    name = models.CharField( max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="sub_categorys", null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class images(models.Model):
    image = models.ImageField(upload_to="image_detail")
    product = models.ForeignKey(detail, on_delete=models.CASCADE,related_name="details_images")
    


class color(models.Model):
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.color
    
    
class size(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
    
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class comment(TimeStamp):
    product = models.ForeignKey(detail, on_delete=models.CASCADE, related_name="comments")
    body =  models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
  
    
class favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(detail, on_delete=models.CASCADE, related_name="product_favorite")
    
    def __str__(self):
        return self.user.full_name
    
    class Meta:
        unique_together = ('user', 'product')
