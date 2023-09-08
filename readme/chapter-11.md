# Extending user registration

[More about messages module](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/)

[More about form validation](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)

[Django built-in validators](https://docs.djangoproject.com/en/5.1/ref/validators/)

## Showing messages to the user
* We're going to utilize `messages` module to show messages to the user.
* Open file `config/settings.py` to enable `messages` module. Add following line on the end of file:
  ```python
  MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
  ```
* Open file `templates/base.html` and dd following code just **before** closing `</body>` tag:
  ```html
  <!-- Previous code -->

  {% block body.js %}
      {% if messages %}
      <script>
          alert('{% for message in messages %}{{ message }}\n{% endfor %}');
      </script>
      {% endif %}
  {% endblock body.js %}
  </body>
  ```
* Open file `registration/views.py`:
  * Import `SuccessMessageMixin` mixin:
    ```python
    from django.contrib.messages.views import SuccessMessageMixin
    ```
  * Add `SuccessMessageMixin` as a parent class to `RegisterUserView` and `success_message` attribute:
    ```python
    class RegisterUserView(SuccessMessageMixin, CreateView):
        # previous code
        success_message = "Account created. You can log in."
    ```
* Now navigate to [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/).
  * Try to register new user.
  * You will see a modal window with message: `Account created. You can log in.`.

## Registration with unique email
* We're going to show how to write custom validation in forms.
* Open file `registration/forms.py`:
  * Add a new method `clean_email` to `RegisterUserForm`:
    ```python
    class RegisterUserForm(UserCreationForm):
        # Previous code
        def clean_email(self):
            email = self.cleaned_data["email"]

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email was used by another user")

            return email
    ```
* Now navigate to [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/).
  * Try to register new user with email address which you've already used for another user.
  * After clicking `Register` you should see `Email was used by another user` error message over `Password` field.
