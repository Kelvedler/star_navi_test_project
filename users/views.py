from django import shortcuts
from rest_framework import generics, viewsets, response, status
from . import serializers, models
import mixins


class Signup(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class Activity(mixins.LastActivityTrackerMixin, viewsets.ViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    def retrieve(self, request, pk=None):
        user = shortcuts.get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user, fields={'last_login': None, 'last_activity': None})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
