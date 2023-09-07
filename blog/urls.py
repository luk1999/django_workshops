from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("<str:slug>,<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("", views.PostIndexView.as_view(), name="index"),
]
