# Authenticating users

[More about forms](https://docs.djangoproject.com/en/5.1/ref/forms/)
[Working with forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

## Display logged in user name
* We want to see logged in user name on every page of our Blog.
* Open `templates/base.html` template.
* Go to `<body>...</body>` section and add following code **before** `{% block body %}`:
  ```html
  {% if user.is_authenticated %}
  <p style="float: right">Logged in as: {{ user.username }}</p>
  {% endif %}
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. If you're still logged in into `Admin Panel`,
then you should see similar message: `Logged in as: <your user name>` in top right corner.

## Create regular user
* Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) page.
* Add new user (click on "Add" button in "Users" section).
* Provide unique `username` and password. Do not change anything in next form.
* **Log off** from `Admin Panel`.

## Turn on login screen
* We want to allow non-Admin users to login. We're going to use `auth` module which is a part of Django package.
* Open file `config/settings.py`.
* Add following line on the end of the file:
  ```python
  LOGIN_REDIRECT_URL = "/"
  ```
  This will force to redirect to main Blog page after finishing login process.
* Open file `config/urls.py`.
* Add `auth` app URLs to `urlpatterns`:
  ```python
  urlpatterns = [
      path("accounts/", include("django.contrib.auth.urls")),
      # ... other URLs
  ]
  ```
* Create template `templates/registration/login.html` with following content:
  ```html
  {% extends "base.html" %}

  {% block body.content %}
  <h2>Log In</h2>
  <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Log In</button>
  </form>
  {% endblock body.content %}
  ```
  This template will be used to render Login form.
* Now navigate to [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/).
  * You should see Login page with `Username` and `Password` fields.
  * Try to login by providing invalid credentials. You should see an error message.
  * Try to login using valid credentials. You should be redirected to main page and see in top right corner.

## Logout URL
* Open file `config/settings.py`.
* Add following line on the end of the file:
  ```python
  LOGOUT_REDIRECT_URL = "/"
  ```
  This will force to redirect to main Blog page after logging out.
* Open `templates/base.html` template.
* Go to `{% if user.is_authenticated %}...{% endif %}` section and add following code:
  ```html
  <p style="float: right">
  {% if user.is_authenticated %}
      Logged in as: {{ user.username }}
      | <a href="{% url 'logout' %}" title="Log out">Log out</a>
  {% else %}
      <a href="{% url 'login' %}" title="Login">Login</a>
  {% endif %}
  </p>
  ```
* Refresh page in web browser. Click on `Log out` button in top right corner. Try to login again.
