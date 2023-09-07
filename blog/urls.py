from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.PostIndexView.as_view(), name="index"),
]
