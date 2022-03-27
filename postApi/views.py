from core.models import Post
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from postApi.serializers import PostSerializer

@api_view(['GET'])
def home(request):
    instance = Post.objects.all().first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id','title','content','greetings'])
        data = PostSerializer(instance).data
    return Response(data)