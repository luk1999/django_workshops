# User registration

## Create `registration` application
* Run command:
  ```bash
  python manage.py startapp registration
  ```
* Current app structure should look like:
  ```
  ├── blog
  |   └── ...
  ├── registration
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
  ├── templates
  |   └── ...
  ├── ...
  └── manage.py
  ```
* Edit `config/settings.py` file and add `registration` app to list `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
      # Built-in Django apps
      "django.contrib.staticfiles",
      "blog",
      "registration",
  ]
  ```

## Create registration form
* Create file `registration/forms.py` with following content:
  ```python
  from django import forms
  from django.contrib.auth.models import User
  from django.contrib.auth.forms import UserCreationForm

  class RegisterUserForm(UserCreationForm):
      ...
  ```
* Open file `registration/views.py` and replace its content by:
  ```python
  from django.contrib.auth.models import User
  from django.urls import reverse_lazy
  from django.views.generic import CreateView
  from registration.forms import RegisterUserForm

  class RegisterUserView(CreateView):
      model = User
      form_class = RegisterUserForm
      success_url = reverse_lazy("blog:index")
      template_name = "registration/register.html"
  ```
* Create template `templates/registration/register.html` with following content:
  ```html
  {% extends "base.html" %}

  {% block body.content %}
      <h2>Create account</h2>
      <form method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <button type="submit">Register</button>        
      </form>
  {% endblock body.content %}
  ```
  This template will be used to render Registration form.
* Create file `registration/urls.py` and add definition for `register` action:
  ```python
  from django.urls import path
  from registration import views

  app_name = "registration"
  urlpatterns = [
      path("register/", views.RegisterUserView.as_view(), name="register"),
  ]
  ```
* Register newly created package for URL Dispatcher. Open file `config/urls.py` and add one more definition for `accounts/` URL:
  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path("admin/", admin.site.urls),
      path("accounts/", include("django.contrib.auth.urls")),
      # Add only line below this comment:
      path("accounts/", include("registration.urls")),
      path("", include("blog.urls")),
  ]
  ```
  Notice that we've registered another package of URLs under the same `accounts/` main URL. 
  You should do that only when you're absolutely sure that suburls are unique in both packages!
* Now navigate to [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/).
  * You should see a form with `Username`, `Password` and `Password confirmation` fields.
  * Try to register new user.

## URL to registration page
* Open `templates/base.html` and look for a login URL. Add link to registration page under it:
  ```html
  <!-- Previous code -->
  <a href="{% url 'login' %}" title="Login">Login</a>
  | <a href="{% url 'registration:register' %}" title="Register">Register</a>
  <!-- Previous code -->
  ```
* Logout. Now you should see a link `Register` next to `Login`.

## Additional fields in Registration form
* We're going to add `Email` field to Registration form.
* Open file `registration/forms.py` and replace its content by:
  ```python
  from django import forms
  from django.contrib.auth.models import User
  from django.contrib.auth.forms import UserCreationForm

  class RegisterUserForm(UserCreationForm):
      email = forms.EmailField(required=True)

      class Meta:
          model = User
          fields = [
              "username",
              "email",
              "password1",
              "password2",
          ]
  ```
  Notice that we have to define subclass `Meta`, which contains `email` field on the list.
  Because `email` field is not required by default, we need to change its properties above `Meta` class.
* Now navigate to [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/).
  * You should see a form with `Username`, `Email`, `Password` and `Password confirmation` fields.
  * Try to register new user.

## (Optional) Homework
* Create a password change form that:
  * Is available to logged in users only
  * It accepts old password and new one (two fields for a new pass)
  * Redirects user to the main page after changing password
* Create an URL to password change form. It should be placed near to `Logout` button.
* **HINT:** You can use `PasswordChangeView` from `django.contrib.auth.views` package. 
Just remember to define success URL and your own template.
