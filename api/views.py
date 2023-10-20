from rest_framework import viewsets

from api.serializers import CommentSerializer, PostSerializer
from blog.models import Comment, Post


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ["post", "created_by"]
