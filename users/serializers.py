from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'status')
        extra_kwargs = {
            'password': {'write_only': True},
            'status': {'read_only': True},
        }
