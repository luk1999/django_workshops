from django.http import HttpResponse

from blog.models import Post


def index(request):
    query = Post.objects.all()
    titles = [post.title for post in query]
    return HttpResponse("<br>".join(titles))


def index_list(request):
    query = Post.objects.all()
    titles = [f"<li>{post.title}</li>" for post in query]
    return HttpResponse(f"<ul>{''.join(titles)}</ul>")
