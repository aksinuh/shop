from typing import Any, Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserProfileSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'username',
            'email',
        )
        
class UserTokenObtainSerialzier(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        user_serialzier = UserProfileSerialzier(self.user)
        data.update(user_serialzier.data)
        return data
    
    
class UserTokenSerialzier(serializers.ModelSerializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    class Meta:
        model = User
        fields = (
            "refresh",
            "access",
            'id',
            'full_name',
            'username',
            'email',
        )