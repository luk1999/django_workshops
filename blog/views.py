from django.http import HttpResponse

from blog.models import Post


def index(request):
    query = Post.objects.all()
    titles = [post.title for post in query]
    return HttpResponse("<br>".join(titles))
