from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("list", views.index_list, name="index_list"),
    path("", views.index, name="index"),
]
