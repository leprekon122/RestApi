from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *


class CreateUserSerialize(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class CreateNewsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'link', 'author_name']


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['username', 'comments', 'name']
