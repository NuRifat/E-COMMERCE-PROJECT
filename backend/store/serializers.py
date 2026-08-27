from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Instead of showing only the category ID, serialize the complete Category object.
    # read_only: You can read category information through this field, but you cannot use this nested field to create/update the category relationship.
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'