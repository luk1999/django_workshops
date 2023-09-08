from django.urls import path
from registration import views

app_name = "registration"
urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="register"),
]
