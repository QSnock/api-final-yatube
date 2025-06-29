from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet, basename='post-comments'
)

jwt_urls = [
    path('create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/', include(jwt_urls)),
]
