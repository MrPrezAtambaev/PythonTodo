from .models import TodoItem, Auth, Login
from rest_framework import serializers
# from rest_framework.authtoken.models import Token


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'completed', 'author')


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'email', 'password', 'password2')


class LoginSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()

    class Meta:
        model = Login
        fields = ('id', 'email', 'password')

    # def get_token(self, obj):
    #     token = Token.objects.create(user=obj)
    #     return token.key
