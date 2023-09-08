from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import RegisterUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy("blog:index")
    template_name = "registration/register.html"
