
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["shop", "name", "slug", "description"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["shop", "category", "name", "slug", "description", "price", "purchase_price", "discount", "stock", "image", "is_active"]
