
from rest_framework import serializers
from .models import CustomUser,Image


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user
    
    




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields ='__all__'
        read_only_fields = ['owner']

# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'user_name', 'email'] # Include other fields as necessary
