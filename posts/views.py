from django.core import exceptions as django_exceptions
from rest_framework import viewsets, response, status, permissions, exceptions as rest_framework_exceptions
from . import serializers, models
import mixins


class PostCreateView(mixins.LastActivityTrackerMixin, viewsets.ViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        request.data['author'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeView(mixins.LastActivityTrackerMixin, viewsets.ViewSet):
    serializer_class = serializers.LikeSerializer
    model_object = models.Like.objects
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, post_id=None):
        request.data['post'] = post_id
        request.data['user'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, post_id=None):
        try:
            like = self.model_object.get(post=post_id, user=request.user)
        except django_exceptions.ObjectDoesNotExist:
            raise rest_framework_exceptions.NotFound(detail={'message': 'User did not like this post.'})
        like.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
