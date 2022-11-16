from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, PostViewSet, like_post

router = routers.SimpleRouter()
router.register('posts',PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_post, name='like_post')
]