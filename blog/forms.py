from django.forms import ModelForm

from blog.models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
