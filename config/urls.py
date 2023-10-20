from django.contrib import admin
from django.urls import include, path

from api.urls import router

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("registration.urls")),
    path("", include("blog.urls")),
]
