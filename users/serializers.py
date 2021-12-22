from rest_framework import serializers
from django.db import transaction
from . import models, jwt


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            user = models.User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
            )
            tokens = jwt.get_tokens_for_user(user)
            user.refresh = tokens['refresh']
            user.access = tokens['access']
        return user
