from media.models import Blog, Comments
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UsernameTelegram


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsernameTelegram
        fields= "__all__"