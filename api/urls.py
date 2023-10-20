from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet)
router.register(r"comments", views.CommentViewSet)
