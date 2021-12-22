from rest_framework.generics import CreateAPIView
from . import serializers


class Signup(CreateAPIView):
    serializer_class = serializers.UserSerializer
