from statistics import mode
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']
    

    
# class UserSerializer(serializers.Serializer):
    
#     class Meta:
#         model = User
#         username = serializers.CharField()
#         password = serializers.CharField()
    
#     def create(self, validated_data):
#         """
#         Create and return a new `User` instance, given the validated data.
#         """
#         return User.objects.create(**validated_data)