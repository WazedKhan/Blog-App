from core.models import Post
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    model_data = Post.objects.all().first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','content'])
    return Response(data)