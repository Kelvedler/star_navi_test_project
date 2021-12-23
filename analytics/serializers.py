from rest_framework import serializers
from posts import models as post_models


class LikeSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = post_models.Like
        fields = ['total']
