from rest_framework import serializers
from products.models import category,detail

class categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = (
            "id",
            "name",
        )
        
        
class detailserializers(serializers.ModelSerializer):
    product = serializers.CharField(source="product.title")
    discount = serializers.CharField(source="discount.rate")
    color = serializers.CharField(source="color.color")
    size = serializers.CharField(source="size.name")
    category= serializers.CharField(source= "product.category.name")
    image = serializers.ImageField(source= "product.image")
    class Meta:
        model = detail
        fields = (
            "id",
            "title",
            "price",
            "Description",
            "product",
            "discount",
            "properties",
            "color",
            "size",
            "display",
            "image",
            "category",
        )
        


