from django.db import models as django_models
from rest_framework import viewsets, response, status
from posts import models as post_models
from . import serializers
import mixins


class LikeView(mixins.LastActivityTrackerMixin, viewsets.ViewSet):
    serializer_class = serializers.LikeSerializer
    queryset = post_models.Like.objects

    def list(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        if not date_from and not date_to:
            timestamp_filter = django_models.Q()
        elif not date_from:
            timestamp_filter = django_models.Q(timestamp__date__lte=date_to)
        elif not date_to:
            timestamp_filter = django_models.Q(timestamp__date__gte=date_from)
        else:
            timestamp_filter = django_models.Q(timestamp__date__range=[date_from, date_to])
        total_likes = self.queryset.filter(timestamp_filter).count()
        serializer = self.serializer_class({'total': total_likes})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
