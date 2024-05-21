from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class UserSignUp(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        raw_password = serializer.validated_data.get('password')
        serializer.validated_data['password'] = make_password(raw_password)
        serializer.save()
