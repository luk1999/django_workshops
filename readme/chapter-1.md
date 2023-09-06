# App creation and configuration

## Create project

* Go to your project directory and enable virtual env:
  ```bash
  cd <your_projects_dir>/django_workshops
  # If you use Pipenv:
  pipenv shell
  # If you use Venv:
  .venv\scripts\activate
  ```
* Create Django project:
  ```bash
  django-admin startproject config ../django_workshops
  ```
* Current app structure should look like:
  ```
  ├── config
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  |   └── wsgi.py
  ├── ...
  └── manage.py
  ```
  * `manage.py` - Script used to run application administrative tasks or user defined tasks
  * `config/settigs.py` - Main application configuration file
  * `config/urls.py` - Configuration of URL dispatcher
  * `config/asgi.py` / `config/wsgi.py` - Main entry point for app server
* Accessing Django shell:
  ```bash
  python manage.py shell
  ```
  ```python
  Python 3.11.4 (main, Jul 19 2023, 09:44:04) [GCC 11.2.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>> from django.conf import settings
  >>> settings.BASE_DIR
  PosixPath('/home/gf2stus_ztb_icb_commerzbank_com/django_workshops')
  ```

## Configure project
Open `config/settigs.py` file and:
* Look for `DEBUG`:
```python
DEBUG = True
```
  Debug should be enabled **only for local development**. You can use projects like [django-environ](https://github.com/joke2k/django-environ) to load settings from `.env` file locally or directly from system env variables on other environments (prod etc)
* Find and replace:
```python
ALLOWED_HOSTS = ["127.0.0.1"]
```
* Look for `TIME_ZONE`:
```python  
TIME_ZONE = "UTC"  
```
  You can change to `CET` if you're sure that it will be used in our (Central Europe) timezone.
* Look for `DATABASES`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```
You can define one or more connections to database. Default one is called obviously `default`. You might define other ones like `products` but you need explictly assign them in models definitions.

## Generate database structure
Run command:
```bash
python manage.py migrate
```

This should create a file `db.sqlite3` inside project directory.

## Run development server
Run command:
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser. You should see Django start page.
