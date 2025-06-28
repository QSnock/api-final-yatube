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

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })
    ),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
