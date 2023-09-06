# Django Admin

[More about Django Admin](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/)

## Create superuser

Superuser is an user that is allowed to all operations in your project.

* Run CLI command:
  ```bash
  python manage.py createsuperuser
  ```
* Type required information:
  ```bash
  (django_workshops) ls-admin:~/django_workshops$ python manage.py createsuperuser
  Username (leave blank to use 'ls-admin'): lukasz
  Email address: lukasz.stuszek@test.com
  Password:
  Password (again):
  This password is too common.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  ```
* Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and enter credentials
* You'll be redirected to main page of Admin Panel, where you can manage users

## Post management in Admin Panel
* Open file `blog/admin.py`
* Change its content to:
  ```python
  from django.contrib import admin

  from blog.models import Post

  admin.site.register(Post)
  ```
* Refresh Admin Panel page. `Blog` app and `Post` model should appear on list.
* Try to add new post

## Showing post information and generating slug
* Open file `blog/admin.py`
* Replace line:
  ```python
  admin.site.register(Post)
  ```
  by:
  ```python
  class PostAdmin(admin.ModelAdmin):
      list_display = ("title", "created_by", "created_at", "updated_at")
      prepopulated_fields = {"slug": ("title",)}

  admin.site.register(Post, PostAdmin)
  ```
* Check view with list of posts
* Try to add new post

## Assigning logged in user to created post
* Open file `blog/admin.py`
* Add `exclude` attribute and `save_model` function to `PostAdmin` class:
  ```python
  class PostAdmin(admin.ModelAdmin): 
      # previous code
      exclude = ("created_by",)

      def save_model(self, request, obj, form, change):
          obj.created_by = request.user
          super().save_model(request, obj, form, change)
  ```
* Check view with list of posts
* Try to add new post
