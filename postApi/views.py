from tkinter.tix import Tree
from core.models import Post
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from postApi import serializers
from postApi.serializers import PostSerializer

@api_view(['GET'])
def home(request):
    instance = Post.objects.all()
    serializer = PostSerializer(instance, many = True).data
    return Response(serializer)


@api_view(['POST'])
def create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response(serializer.data)
