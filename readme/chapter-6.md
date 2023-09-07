# Show post content

We're going to create new URL, which will be accessible under URL: 
[http://127.0.0.1:8000/<post_id>/](http://127.0.0.1:8000/<post_id>/).

## Render post content in template
* Create file `templates/blog/detail.html` with following content:
  ```html
  <h1>{{ object.title }}</h1>
  <p><small>Written by: {{ object.created_by }}</small></p>
  <p><small>Created at: {{ object.created_at }}, Updated at: {{ object.updated_at }}</small></p>
  <p>{{ object.content|linebreaksbr }}</p>
  ```
* Open file `blog/views.py`.
* Extend import section by adding `ListView`:
  ```python
  from django.views.generic import DetailView, ListView
  ```
* Then add `PostDetailView` on the bottom of file:
  ```python
  class PostDetailView(DetailView):
      template_name = "blog/detail.html"
      model = Post
  ```
* Open file `blog/urls.py`.
* Add a definition for `detail` view (make sure that it is above `index` URL):
  ```python
  urlpatterns = [
      path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
      path("", views.PostIndexView.as_view(), name="index"),
  ]
  ```
* Open [http://127.0.0.1:8000/1](http://127.0.0.1:8000/1) in web browser. You should see a `Post` along with its content
and additional information.

## Dynamic URLs
* Open file `templates/blog/detail.html` and add at the bottom of page:
  ```html
  <a href="{% url 'blog:index' %}" title="List of posts">Return to list of posts</a>
  ```
* Open file `templates/blog/index.html` and replace:
  ```html
  <h2>{{ post.title }}</h2>
  ```
  by:
  ```html
  <h2>
      <a href="{% url 'blog:detail' post.pk %}" title="Show {{ post.title }}">{{ post.title }}</a>
  </h2>
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see a list of posts.
When you click on post title, you'll be redirected to post content page. This page should have 
`Return to list of posts` link, that will redirect you again to the list of posts.

## Adding more params to URL
* Open file `blog/urls.py`.
* Add one more parameter for `detail` view: `<str:slug>`, to make URL more search engine friendly:
  ```python
  urlpatterns = [
      path("<str:slug>,<int:pk>/", views.PostDetailView.as_view(), name="detail"),
      # ... other URLs
  ]
  ```
* Open file `templates/blog/index.html` and look for:
  ```html
  <h2>
      <a href="{% url 'blog:detail' post.pk %}" title="Show {{ post.title }}">{{ post.title }}</a>
  </h2>
  ```
  Include `slug` parameter (order is important):
  ```html
  <h2>
      <a href="{% url 'blog:detail' post.slug post.pk %}" title="Show {{ post.title }}">{{ post.title }}</a>
  </h2>
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. Check how the links to the posts look currently.
You should see something like: [http://127.0.0.1:8000/my-new-post,1](http://127.0.0.1:8000/my-new-post,1)

## (Optional) Homework
* Add additional section `Stats` on bottom of main page (under the list of posts).
* It should be visible only if at least two posts were created.
* It should contain URLs to the newest and the oldest post on our blog.
* Page should render following content:
  ```
  <!-- Render only if at least 2 posts exist -->
  <h1>Stats<h1>
  <p>
    Newest post: <a href="..." title="Show newest post">Newest post title</a>
  </p>
  <p>
    Oldest post: <a href="..." title="Show oldest post">Oldest post title</a>
  </p>
  ```
