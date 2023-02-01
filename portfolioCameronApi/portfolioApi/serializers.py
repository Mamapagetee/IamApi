from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_image', 'post_title', 'post_content']
