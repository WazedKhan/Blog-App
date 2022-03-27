from dataclasses import fields
from pyexpat import model
from core.models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content','author','created_at','greeting']
        