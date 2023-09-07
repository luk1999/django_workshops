from django.views.generic import DetailView, ListView

from blog.models import Post


class PostIndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.order_by("-created_at")


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post
