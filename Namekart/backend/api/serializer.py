from .models import Notes
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class NotesSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model=Notes

class UserSERIALIZER(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # hash password
        user.save()
        return user