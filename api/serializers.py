from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Category, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

   


   

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            # 'imageUrl',
            'status',
            'date_created'
        )
        model = Product


