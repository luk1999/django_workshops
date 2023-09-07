from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]
