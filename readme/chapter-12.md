# Custom forms for authorized users

[More about creating model based forms](https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/)

In this chapter we're going to create comment form which is available to registered users only.

## Comment form
* Create file `blog/forms.py` with following content:
  ```python
  from django.forms import ModelForm
  from blog.models import Comment

  class CreateCommentForm(ModelForm):
      class Meta:
          model = Comment
          fields = ["comment"]
  ```
* Now we have to use `CreateView` as parent class in order to be able to use create comment form.
  Open file `blog/views.py` and:
  * Change imports:
    ```python
    from django.views.generic import CreateView, DetailView, ListView

    from blog.forms import CreateCommentForm  # Our new form
    from blog.models import Comment, Post
    ```
* Create `CreateCommentView`: 
  * Import method `reverse` from `django.urls` package
  * with parent class `CreateView`
  * assign `CreateCommentForm`
  * assign related post and logged in user to newly created comment in `form_valid` method
  * add `get_success_url` which redirect us to post detail view after posting comment
  ```python
  # Previous imports
  from django.urls import reverse

  # Previous code

  class CreateCommentView(CreateView):
      template_name = "blog/comment.html"
      model = Comment
      form_class = CreateCommentForm

      def form_valid(self, form):
          form.instance.post_id = self.kwargs["pk"]
          form.instance.created_by = self.request.user
          return super().form_valid(form)

      def get_success_url(self) -> str:
          return reverse("blog:detail", kwargs={"slug": self.kwargs["slug"], "pk": self.kwargs["pk"]})
  ```
* Create file `templates/blog/comment.html` and add following code:
  ```html
  {% extends "base.html" %}

  {% block title %}Add your comment{% endblock title %}

  {% block body.content %}
      <h1>Add your comment</h1>
      <form method="post">
          {% csrf_token %}
          {{ form }}
          <button type="submit">Add comment</button>
      </form>    
  {% endblock body.content %}
  ```
* Edit `blog/urls.py` and add URL to form in URL dispatcher config:
  ```python
  urlpatterns = [
      path("<str:slug>,<int:pk>/comment/", views.CreateCommentView.as_view(), name="comment"),
      # ... other URLs
  ]
  ```
* Test adding of comment for logged in (authenticated) user:
  * Open any post details page.
  * Add in web browser URL bar `comment/` (eg: `http://127.0.0.1:8000/my-first-day,1/` should be replaced by `http://127.0.0.1:8000/my-first-day,1/comment/`)
  * Create comment form should appear.
  * Try to add new comment.
  * You should be redirected to post detail page and new comment appear on page.
* Test adding of comment for logged out (anonymous) user:
  * Open any post details page.
  * Add in web browser URL bar `comment/` (eg: `http://127.0.0.1:8000/my-first-day,1/` should be replaced by `http://127.0.0.1:8000/my-first-day,1/comment/`)
  * Create comment form should appear.
  * Try to add new comment.
  * You should see an error page.

## Allow only logged in users to create comments
* Open `templates/blog/detail.html` and add URL to comment form just under header `Comments`:
  ```html
  <h2>Comments</h2>

  <!-- URL to comment form is shown only when user is logged in -->
  {% if user.is_authenticated %}
  <p><a href="{% url 'blog:comment' object.slug object.pk %}">Add your comment</a></p>
  {% endif %}
  <!-- end of comment form URL -->

  {% for comment in comments %}
  ```
* Open `blog/views.py` and add code which will force anonymous users to log in before using comment form:
  * Import `LoginRequiredMixin`:
    ```python
    from django.contrib.auth.mixins import LoginRequiredMixin
    ```
  * Inherit from `LoginRequiredMixin` in `CreateCommentView` class:
    ```python
    class CreateCommentView(LoginRequiredMixin, CreateView):
        # previous code
    ```
* Test adding of comment for logged out (anonymous) user:
  * Open any post details page.
  * Add in web browser URL bar `comment/` (eg: `http://127.0.0.1:8000/my-first-day,1/` should be replaced by `http://127.0.0.1:8000/my-first-day,1/comment/`)
  * You should be redirected to login page.
