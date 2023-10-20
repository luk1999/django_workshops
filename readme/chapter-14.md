# REST API

We're going to utilize [DRF: Django REST Framework](https://www.django-rest-framework.org/)
for creation of REST API for our Blog.

## Installation
* Install `djangorestframework`:
  ```bash
  pip install djangorestframework
  # or
  pipenv install djangorestframework
  ```
* Open `config/settings.py` and
  * Add to `INSTALLED_APPS` `rest_framework`:
    ```python
    INSTALLED_APPS = [
        # Django apps        
        "crispy_forms",
        "crispy_bootstrap5",
        "rest_framework",
        # Apps defined by you
    ]
    ```
  * Add at the end of file:
    ```python
    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        ],
    }
    ```

## URL router configuration
* Create Python package `api` (remember about `__init__.py` file inside):
* Create file `api/urls.py` with following content:
  ```python
  from rest_framework import routers

  router = routers.DefaultRouter()
  ```
* Include router configuration in URL dispatcher configuration. Update file `config/urls.py`:
  ```python
  # Previous imports should be there

  from api.urls import router  # Import router
  
  urlpatterns = [
      path("api/v1/", include(router.urls)),
      # previous URLS
  ]
  ```
* Run Django development server and then navigate to `http://127.0.0.1:8000/api/v1/`. 
  You should see a default DRF welcome page.

## Define read-only API endpoint with posts
* Create file `api/serializers.py` with following content:
  ```python
  from rest_framework import serializers

  from blog.models import Post

  class PostSerializer(serializers.ModelSerializer):
      class Meta:
          model = Post
          fields = (
              "id",
              "title",
              "slug",
              "content",
              "created_by",
              "created_at",
              "updated_at",
          )
  ```
* Create file `api/views.py`:
  ```python
  from rest_framework import viewsets

  from api.serializers import PostSerializer
  from blog.models import Post

  class PostViewSet(viewsets.ReadOnlyModelViewSet):
      queryset = Post.objects.all()
      serializer_class = PostSerializer
  ```
* Open `api/urls.py` and:
  * Import `views`:
    ```python
    from api import views
    ```
  * Add `PostViewSet` to URLs definition:
    ```python
    router = routers.DefaultRouter()
    # Add PostViewSet to URL definitions
    router.register(r"posts", views.PostViewSet)
    ```
* Open webbrowser and navigate to:
  * `http://127.0.0.1:8000/api/v1/posts/` - you should see a list of posts displayed in preformatted form.
  * `http://127.0.0.1:8000/api/v1/posts/1/` - you should see a single post displayed in preformatted form.
  * `http://127.0.0.1:8000/api/v1/posts/?format=json` - you should see a list of posts as a JSON.
  * You can also use Postman (or similar tool) to open `http://127.0.0.1:8000/api/v1/posts/`. 
    It will show data as JSON without preformatting.

### Show related field
We would like to see user's name instead of its PK.

* Open file `api/serializers.py` and:
  * Import `User` model:
  ```python
  from django.contrib.auth.models import User
  ```
  * Define `AuthorSerializer`:
  ```python
  class AuthorSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = (
              "first_name",
              "last_name",
              "username",
          )
  ```
  * Use `AuthorSerializer` in `PostSerializer`:
  ```python
  class PostSerializer(serializers.ModelSerializer):
      created_by = AuthorSerializer()

      class Meta:
          # Previous code
  ```
* Open file `api/views.py` and extend queryset:
  ```python
  class PostViewSet(viewsets.ReadOnlyModelViewSet):
      # Add select_related
      queryset = Post.objects.select_related("created_by").all()
      serializer_class = PostSerializer
  ```
* Open webbrowser and navigate to `http://127.0.0.1:8000/api/v1/posts/`. 
  You should see a list of posts with first, last and username of their authors.

## Define API endpoint with comments
* Open file `api/serializers.py` and:
  * Import `Comment` model:
    ```python
    from blog.models import Comment, Post
    ```
  * Define `CommentSerializer`:
    ```python
    class CommentSerializer(serializers.ModelSerializer):
        created_by = AuthorSerializer()

        class Meta:
            model = Comment
            fields = (
                "id",
                "post",
                "comment",
                "created_by",
                "created_at",
            )
    ```
* Open file `api/views.py` and:
  * Import `Comment` model and `CommentSerializer`:
    ```python
    from api.serializers import CommentSerializer, PostSerializer
    from blog.models import Comment, Post
    ```
  * Define `CommentViewSet`:
    ```python
    class CommentViewSet(viewsets.ModelViewSet):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
    ```
  * Register `CommentViewSet` in `api/urls.py`:
    ```python
    router.register(r"comments", views.CommentViewSet)
    ```
* Open webbrowser and navigate to:
  * `http://127.0.0.1:8000/api/v1/comments/` - you should see a list of comments displayed in preformatted form.
  * `http://127.0.0.1:8000/api/v1/comments/1/` - you should see a single comments displayed in preformatted form.
  * Repeat both operations when you're logged in (you should see a create or update form on the bottom) and logged out.

## Generic filtering

### Django filters installation

* Install `djangorestframework`:
  ```bash
  pip install django-filter
  # or
  pipenv install django-filter
  ```
* Open `config/settings.py` and
  * Add to `INSTALLED_APPS` `django_filters`:
    ```python
    INSTALLED_APPS = [
        # Django apps
        "crispy_forms",
        "crispy_bootstrap5",
        "rest_framework",
        "django_filters",
        # Apps defined by you
    ]
    ```
  * Find `REST_FRAMEWORK` dictionary and add one more key:
    ```python
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    ```
    This will set `django-filter` as default filtering backend for all API endpoints.

### Generic filtering in `CommentViewSet`

* Open `api/views.py` and look for `CommentViewSet`. Add following the attribute:
  ```python
  class CommentViewSet(viewsets.ModelViewSet):
      # Previously defined attrs
      filterset_fields = ["post", "created_by"]
  ```
* Open webbrowser and navigate to:
  * `http://127.0.0.1:8000/api/v1/comments/?post=1` - you should see a list of comments assigned to post #1.
