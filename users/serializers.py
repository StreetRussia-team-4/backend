from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'status')
        extra_kwargs = {
            'password': {'write_only': True},
            'status': {'read_only': True},
        }
