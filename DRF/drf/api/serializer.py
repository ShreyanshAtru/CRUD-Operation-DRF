from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registration details and used inbuilt User model
    Password confirmation is an extra field to vaild the password
    """

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password_confirmation = serializers.CharField(max_length=128, write_only=True)

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirmation"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password_confirmation": {"write_only": True},
        }


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
