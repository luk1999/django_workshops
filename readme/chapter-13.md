# HTML and CSS customization

We're going to use (Twitter) Bootstrap as our frontend CSS framework.

[More about Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

## Configuring static files
Static files like CSS or Javascript has to be stored in your project. 
We're going to use `static` subdirectory for that.

* Create subdirectory `static` in your project.
* Open `config/settings.py` file and add at the end of file:
  ```python
  STATICFILES_DIRS = [
      BASE_DIR / "static",
  ]
  ```
* Download file [bootstrap.min.css](https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css) and save in `static/css/` directory.
* Download file [bootstrap.bundle.min.js](https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js) and save in `static/js/` directory.
* Current app structure should look like:
  ```
  ├── blog
  ├── config
  ├── registration
  ├── static
  │   ├── css
  │   │   └── bootstrap.min.css
  |   └── js
  │   │   └── bootstrap.bundle.min.js
  ├── templates
  ├── ...
  └── manage.py
  ```

## Adding Bootstrap to templates
* Open `templates/base.html` and change:
  * Add `{% load static %}` template tag at the beginning of file:
    ```html
    {% load static %}<!doctype html>
    <!-- previous code -->
    ```
  * Include `bootstrap.min.css` file just before closing `</head>` tag:
    ```html
        <!-- previous code -->
        <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    </head>
    ```
  * Include `bootstrap.bundle.min.js` just before closing `</body>` tag:
    ```html
    
        <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    </body>
    ```
  * Open main page (`http://127.0.0.1:8000/`). You should notice that style of page changed.

## Using Bootstrap styles for base template

[More about Bootstrap layouts and containers](https://getbootstrap.com/docs/5.3/layout/)
[More about Bootstrap components](https://getbootstrap.com/docs/5.3/components/)

* Open `templates/base.html` and change:
  * Add container with margins for page content (it should start just after `<body>` and end before Javascript import):
  ```html
  <body>
      <div class="container">
      <!-- previous code -->
      </div>

      <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
  </body>
  ```
  * Create page header using `nav` component. 
    * Remove following code:
      ```html
      <p style="float: right">
          {% if user.is_authenticated %}
              Logged in as: {{ user.username }}
              | <a href="{% url 'logout' %}" title="Log out">Log out</a>
          {% else %}
               <a href="{% url 'login' %}" title="Login">Login</a>
               | <a href="{% url 'registration:register' %}" title="Register">Register</a>
          {% endif %}
      </p>      
      ```
      ```html
      <p>
          <h1><a href="{% url 'blog:index' %}" title="My blog">My blog</a></h1>
          <hr>
      </p>
      ```
    * Add following code between `<body>` and `<div class="container">`:
      ```html
      <nav class="navbar navbar-expand navbar-light bg-light">
          <div class="container">
              <a class="navbar-brand" href="{% url 'blog:index' %}" title="My blog">My blog</a>

              <div class="justify-content-end">
                  <ul class="navbar-nav">
                  {% if user.is_authenticated %}
                      <li class="nav-item">
                          <span class="nav-link">Logged in as: {{ user.username }}</span>
                      </li>
                      <li class="nav-item">
                          <a class="nav-link" href="{% url 'logout' %}" title="Log out">Log out</a>
                      </li>
                  {% else %}
                      <li class="nav-item">
                          <a class="nav-link" href="{% url 'login' %}" title="Login">Login</a>
                      </li>
                      <li class="nav-item">
                          <a class="nav-link" href="{% url 'registration:register' %}" title="Register">Register</a>
                      </li>
                  {% endif %}
                  </ul>
              </div>
          </div>
      </nav>      
      ```

## Using Bootstrap styles for main page
* Open `templates/blog/index.html` and replace:
  ```html
  <p>Could not find any posts.</p>
  ```
  by:
  ```html
  <div class="alert alert-info">Could not find any posts.</div>
  ```

## Using Bootstrap styles for post details page
* Open `templates/blog/detail.html` and change:
  * Look for `Return to list of posts` URL and `Add your comment`. Add CSS classes `btn btn-light` to both of them:
  ```html
  <a class="btn btn-light" href="{% url 'blog:index' %}" title="List of posts">Return to list of posts</a>
  ```
  ```html
  <a class="btn btn-light" href="{% url 'blog:comment' object.slug object.pk %}">Add your comment</a>
  ```
  * Put `<h1>{{ object.title }}</h1>` inside `div` with `row` CSS class:
  ```html
  <div class="row">
      <h1>{{ object.title }}</h1>
  </div>
  ```
  * Put another `div` with `row` CSS class under title and close it just before `{% endblock body.content %}`:
  ```html
  <div class="row">
      <h1>{{ object.title }}</h1>
  </div>

  <div class="row">
      <!-- Whole content of the page (under title) -->
  </div>
  {% endblock body.content %}
  ```
  * Now we're going to put the main content of page (without comments) on left side of page and comments on right:
  ```html
  <div class="row">
      <h1>{{ object.title }}</h1>
  </div>

  <div class="row">
      <div class="col">
          <!-- Your post content -->
          <a class="btn btn-light" href="{% url 'blog:index' %}" title="List of posts">Return to list of posts</a>
      </div>

      <div class="col-xl-3 col-lg-4 col-md-6">
          <h2>Comments</h2>
          <!-- Link to add comment form and list of comments -->
      </div>
  </div>
  {% endblock body.content %}
  ```
  * Finally replace:
    ```html
    <p>Could not find any comments.</p>
    ```
    by:
    ```html
    <div class="alert alert-info">Could not find any comments.</div>
    ```

## Using Bootstrap for styling forms

We're going to use [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5) for 
styling forms.

[More about Bootstrap forms](https://getbootstrap.com/docs/5.3/forms/)

* Install `crispy-bootstrap5`
  ```bash
  pip install crispy-bootstrap5
  # or
  pipenv install crispy-bootstrap5
  ```
* Open `config/settings.py` and
  * Add to `INSTALLED_APPS` `crispy_forms` and `crispy_bootstrap5`:
    ```python
    INSTALLED_APPS = [
        # Django apps        
        "crispy_forms",
        "crispy_bootstrap5",
        # Apps defined by you
        "blog",
        "registration",
    ]
    ```
  * Add at the end of file:
    ```python    
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    ```
* Open `templates/blog/comment.html` and:
  * Load `crispy_forms_tags` template tag just after `{% extends ... %}`:
    ```html
    {% extends "base.html" %}
    {% load crispy_forms_tags %}
    ```
  * Replace
    ```html
    {{ form }}
    ```
    by:
    ```html
    {{ form|crispy }}
    ```
  * And finally add CSS classes to `Add comment` button:
    ```html
    <button class="btn btn-primary float-end" type="submit">Add comment</button>
    ```
* Do the same changes for `templates/registration/login.html` and `templates/registration/register.html`.
