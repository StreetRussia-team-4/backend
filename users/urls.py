from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

v1_users_router = DefaultRouter()
v1_users_router.register('', UserViewSet, basename='users')
