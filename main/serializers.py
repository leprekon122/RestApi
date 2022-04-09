from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User
from .models import *


class CreateUserSerialize(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class CreateNewsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'link', 'author_name']


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'username', 'comments', 'name']

