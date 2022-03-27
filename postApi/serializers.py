from core.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    greeting = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = ['title','content','author','created_at','greeting']
        
    def get_greeting(self, obj):
        try:
            return obj.greeting()
        except:
            return None