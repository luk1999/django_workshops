from django.views.generic import ListView

from blog.models import Post


class PostIndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.order_by("-created_at")
