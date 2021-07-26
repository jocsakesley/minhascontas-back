from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from minhascontas.authentication.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserPostSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'birthday', 'gender')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TokenUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email")