# Django Templates

[More about Django Templates](https://docs.djangoproject.com/en/5.1/topics/templates/)
[More about Django Template tags and filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)
[More about writing db queries](https://docs.djangoproject.com/en/5.1/topics/db/queries/)

## Configure templates directory
* Create directory `templates` inside project.
* Open `config/settings.py` file.
* Search for `TEMPLATES` variable. You should see something like:
  ```python
  TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [],
          # ...
  ```
* We need to add path to the directory, that we've created (we can use `BASE_DIR` variable to get root project dir):
  ```python
  TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [BASE_DIR / "templates"],
          # ...
  ```

## Render post list in template
* Create subdirectory `blog` inside `templates` directory.
* Create file `templates/blog/index.html` with following content:
  ```html
  <h1>Posts</h1>

  {% for post in posts %}
  <h2>{{ post.title }}</h2>
  {% empty %}
  <p>Could not find any posts.</p>
  {% endfor %}
  ```
* Open file `blog/views.py` and replace its content by:
  ```python
  from django.shortcuts import render
  from blog.models import Post

  def index(request):
      posts = Post.objects.all()
      return render(request, "blog/index.html", {"posts": posts})
  ```
  This will get a list of posts (`SELECT * FROM blog_post`) and render them using `index.html` template.
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a `Post` header and list of posts that you've created under it. If you haven't created any post yet, you'll get a message `Could not find any posts.`.

## Show posts and related information
* Open file `templates/blog/index.html`.
* Look for section:
  ```html
  {% for post in posts %}
  <h2>{{ post.title }}</h2>
  {% empty %}
  ```
* Replace it by:
  ```html
  {% for post in posts %}
  <h2>{{ post.title }}</h2>
  <small>
      Created at: {{ post.created_at }},
      Updated at: {{ post.updated_at }}
  </small>
  <p>{{ post.content }}</p>
  {% empty %}
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a `Post` header and list of posts that you've created under it along with creation and update date and content.

## Changing apperance of the post list

### Show newest on the top
* Open file `blog/views.py`.
* Replace line:
  ```python
  posts = Post.objects.all()
  ```
  by:
  ```python
  posts = Post.objects.order_by("-created_at")
  ```
  This will get a list of posts sorted in descending order (`SELECT * FROM blog_post ORDER BY created_at DESC`).

### Replace line breaks in content to `<br>`
* Open file `templates/blog/index.html`.
* Replace line:
  ```html
  <p>{{ post.content }}</p>
  ```
  by:
  ```html
  <p>{{ post.content|linebreaksbr }}</p>
  ```

### Show only an abstract of the post
* Open file `templates/blog/index.html`.
* Replace line:
  ```html
  <p>{{ post.content|linebreaksbr }}</p>
  ```
  by:
  ```html
  <p>{{ post.content|linebreaksbr|truncatewords_html:15 }}</p>
  ```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a `Post` header and list of posts that you've created under it along with newest posts and only abstracts of posts.

## Class-based views
* Open file `blog/views.py`.
* Replace its content by:
  ```python
  from django.views.generic import ListView
  from blog.models import Post

  class PostIndexView(ListView):
      template_name = "blog/index.html"
      model = Post
      queryset = Post.objects.order_by("-created_at")
  ```
* Open file `blog/urls.py`.
* Change `patterns` from:
  ```python
  urlpatterns = [
      path("", views.index, name="index"),
  ]
  ```
  to:
  ```python
  urlpatterns = [
      path("", views.PostIndexView.as_view(), name="index"),
  ]
  ```
* Open file `templates/blog/index.html`.
* Change line:
  ```python
  {% for post in posts %}
  ```
  to:
  ```python
  {% for post in object_list %}
  ```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see exactly the same result as previously.
