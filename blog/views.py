from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from blog.forms import CreateCommentForm
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


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "blog/comment.html"
    model = Comment
    form_class = CreateCommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("blog:detail", kwargs={"slug": self.kwargs["slug"], "pk": self.kwargs["pk"]})
