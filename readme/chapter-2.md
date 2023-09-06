# First application and model

## Create `blog` application
* Run command:
  ```bash
  python manage.py startapp blog
  ```
* Current app structure should look like:
  ```
  ├── blog
  │   ├── migrations
  │   │   └── __init__.py
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── tests.py
  │   ├── views.py
  |   └── ...
  ├── config
  |   └── ...
  ├── ...
  └── manage.py
  ```
* Edit `config/settings.py` file and add `blog` app to list `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
      # Built-in Django apps
      "django.contrib.staticfiles",
      "blog",
  ]
  ```

## Create `Post` model
* Open `blog/models.py` file
* Change its content to:
  ```python
  from django.conf import settings
  from django.db import models

  User = settings.AUTH_USER_MODEL

  class Post(models.Model):      
      title = models.CharField(max_length=100)
      slug = models.SlugField(max_length=100)
      content = models.TextField()
      created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
          return self.title
  ```

## Create and apply database migrations
* Run command to create migration file:
  ```bash
  python manage.py makemigrations
  ```
* File `blog/migrations/0001_initial.py` should be created
* Run command to apply changes on database:
  ```bash
  python manage.py migrate
  ```

## (Optional) Homework
* Look for a tool to view SQLite databases and use it to open generated db file.
* Check the structure - it should be similar to:
  ```
  ├── auth_group
  ├── auth_group_permissions
  ├── auth_permission
  ├── auth_user
  ├── auth_user_groups
  ├── auth_user_permission
  ├── blog_post
  ├── django_admin_log
  ├── django_content_type
  ├── django_migrations
  └── django_session
  ```
* Notice that there are groups of tables (grouped by prefix):
  * `auth_*` - used by built-in Django `auth` module (authentication and authorization)
  * `django_*` - used by Django or Admin Panel to store additional information
  * `blog_*` - tables for our application `blog`
* Browse tables data to see their content.
