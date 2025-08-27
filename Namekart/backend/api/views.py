from django.shortcuts import render
from .serializer import NotesSerializer,UserSERIALIZER
from .models import Notes
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class NotesView(generics.ListCreateAPIView):
    serializer_class=NotesSerializer
    queryset=Notes.objects.all()
    permission_classes=[IsAuthenticated]

class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=NotesSerializer
    lookup_field='pk'
    queryset=Notes.objects.all()
    permission_classes=[IsAuthenticated]

class UserView(generics.CreateAPIView):
    serializer_class=UserSERIALIZER
    model=User.objects.all()