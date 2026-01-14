from django.shortcuts import render
from rest_framework import generics
from .serialzier import TaskSerializer,CommentSerializer
from .models import Task,Comment

class TasksView(generics.ListCreateAPIView):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    lookup_field='pk'
    queryset=Task.objects.all()

class CommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset=Comment.objects.all()


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_field='pk'
    queryset=Comment.objects.all()



