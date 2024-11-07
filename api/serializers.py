from django.core.exceptions import ValidationError
from rest_framework import serializers
from Wing.models import Wing_One
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'], username=clean_data['username'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class Win_One_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Wing_One
        fields = '__all__'