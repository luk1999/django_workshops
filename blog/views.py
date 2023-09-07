from django.views.generic import DetailView, ListView

from blog.models import Comment, Post


class PostIndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.order_by("-created_at")


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_id = self.object.pk
        context["comments"] = Comment.objects.filter(post_id=post_id).order_by("-created_at")

        return context
