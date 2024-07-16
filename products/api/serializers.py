from rest_framework import serializers
from products.models import category,detail,product,favorite

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
        
class detailCreateserializers(serializers.ModelSerializer):
    class Meta:
        model = detail
        fields = (
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
        )


class productserializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = (
            "title",
            "category",
            "image",
        )

class favoriteserializers(serializers.ModelSerializer):
    image = serializers.ImageField(source= "product.image")
    title = serializers.CharField(source="product.title")
    price = serializers.FloatField(source="detail.discounted_price")
    class Meta:
        model = favorite
        fields = (
            "image",
            "title",
            "price",
        )