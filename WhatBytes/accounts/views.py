from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from accounts.serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

