# Template inheritance and blocks

If you open any of pages on our Blog and display its source code (use context menu after right click or try CTRL+U), you'll see that generated code is not complete.
There are some HTML tags, that should be included on every page. Since we'd preferre to do that just once, we'll define single main template and use it as base for all our view templates.

[More about blocks and template inheritance](https://docs.djangoproject.com/en/5.1/ref/templates/language/#template-inheritance)

## Create main template
* Create file `templates/base.html` with following content:
  ```html
  <!doctype html>
  <html>
  <head>
      <title>{% block title %}DjBlog{% endblock %}</title>
      <meta name="description" content="Blog written in Django">
      <meta name="keywords" content="tutorial django blog">
  </head>
  <body>      
      {% block body.content %}
      {% endblock body.content %}
  </body>
  </html>
  ```
* Open file `templates/blog/index.html`.
* Put the content of the file inside two tags:
  ```html
  {% block body.content %}
      Here goes your previous template content
  {% endblock body.content %}
  ```
* Add name of base template as a first line on the top of the file:
  ```html
  {% extends "base.html" %}
  ```
* Open file `templates/blog/detail.html`.
* Put the content of the file inside two tags:
  ```html
  {% block body.content %}
      Here goes your previous template content
  {% endblock body.content %}
  ```
* Add name of base template as a first line on the top of the file:
  ```html
  {% extends "base.html" %}
  ```
* Reload page:
  * Check current page title. It should be `DjBlog` now (previously it was empty).
  * Check current page source code. You should see that missing tags like `<html>`, `<body>` etc are returned.

## Adding content that is shown on every page
* We're going to add blog title on top, which will be shown on every blog page.
* Open file `templates/base.html`.
* Go to `<body>...</body>` section.
* Replace it by:
  ```html
  <body>
      {% block body %}
          <p>
              <h1><a href="{% url 'blog:index' %}" title="My blog">My blog</a></h1>
              <hr>
          </p>
          {% block body.content %}
          {% endblock body.content %}
      {% endblock body %}
  </body>
  ```
* Reload page:
  * You should see `My blog` link on the top of every page.

## Inheriting block content from parent template
* We're going to add title of post in `<title></title>` HTML tag.
* Open file `templates/blog/detail.html`.
* Put following code **under** line `{% extends "base.html" %}`:
  ```html
  {% block title %}{{ block.super }}: {{ post.title }}{% endblock title %}
  ```
* Go to any post page details:
  * Check current page title. It should be something like `DjBlog: My new post` now (previously it was `DjBlog`).

## (Optional) Homework
* Meta tags `description` and `keywords` (inside `<head>...</head>`) have hardcoded `content` value:
  ```html
  <head>
    <title>{% block title %}DjBlog{% endblock %}</title>
    <meta name="description" content="Blog written in Django">
    <meta name="keywords" content="tutorial django blog">
  </head>
  ```
* Define ability to set dynamic `content` for both meta tags (**HINT: use blocks**).
* Define custom content values for meta tags on subpages:
  * List of posts (`index.html`):
    * description: `List of all my posts`
    * keywords: it should have all keywords from base template (inherited) and one more at the end: `posts`
  * Post view (`detail.html`):
    * description: `My new post: (title of my post)`
    * keywords: same as in base template
