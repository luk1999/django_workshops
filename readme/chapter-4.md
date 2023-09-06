# Listing posts

## Create view function
* Open file `blog/views.py`
* Replace its content by:
  ```python
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Here should be a list of posts")
  ```

## Create URL definitions
* Create file `blog/urls.py`
* Replace its content by:
  ```python
  from django.urls import path
  from blog import views

  app_name = "blog"
  urlpatterns = [
      path("", views.index, name="index"),
  ]
  ```
* Open file `config/urls.py`
* Replace its content by:
  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path("admin/", admin.site.urls),
      path("", include("blog.urls")),
  ]
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a message `Here should be a list of posts`.

## Return list of posts
* Open file `blog/views.py`
* Replace its content by:
  ```python
  from django.http import HttpResponse
  from blog.models import Post

  def index(request):
      query = Post.objects.all()
      titles = [post.title for post in query]
      return HttpResponse("<br>".join(titles))
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a list of posts that you've created.

## (Optional) Homework
* Create a new view called `index_list`, which will return an unordered HTML list.
* Make it accessible under url `/list`.
* Page should render following content:
  ```
  <h1>My Posts<h1>
  <ul>
    <li>My first post</li>
    <li>My second post</li>
    <li>...</li>
  </ul>
  ```
* **Remember about restarting Django development server after adding new URL!**
