from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Comment, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
        )


class CommentSerializer(serializers.ModelSerializer):
    created_by = AuthorSerializer()

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "comment",
            "created_by",
            "created_at",
        )


class PostSerializer(serializers.ModelSerializer):
    created_by = AuthorSerializer()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "content",
            "created_by",
            "created_at",
            "updated_at",
        )
