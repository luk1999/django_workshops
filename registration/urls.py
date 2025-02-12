from django.urls import path
from registration import views

app_name = "registration"
urlpatterns = [
    path("change-password/", views.PasswordChangeView.as_view(), name="change_password"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
]
