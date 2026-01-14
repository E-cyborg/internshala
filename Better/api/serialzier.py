from rest_framework.serializers import ModelSerializer
from .models import Task,Comment



class CommentSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Comment

class TaskSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        fields = "__all__"
        model = Task