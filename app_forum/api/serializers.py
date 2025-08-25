from app_forum.models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='pk')
    class Meta:
        model = Post
        fields = ['id','url', 'title', 'author', 'content', 'created_at', 'comments']
        read_only_fields = ['author', 'created_at']

