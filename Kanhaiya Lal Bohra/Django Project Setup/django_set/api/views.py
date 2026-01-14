from django.shortcuts import render
from rest_framework import generics,status
from .serializers import BlogSerializer, CommentSerializer,LoginSerializer,TelegramSerializer
from media.models import Blog, Comments
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import UsernameTelegram


class BlogsView(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer
    


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'
    
class BlogView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer



class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # ✅ Check if user is already authenticated
        if request.user and request.user.is_authenticated:
            return Response(
                {"detail": "You are already logged in."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        

class ProctedView(generics.ListCreateAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()
    

class TelegramUser(generics.ListCreateAPIView):
    serializer_class=TelegramSerializer
    queryset=UsernameTelegram.objects.all()
    