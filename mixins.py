from rest_framework import viewsets
from rest_framework_simplejwt import exceptions
from django.utils import timezone


class LastActivityTrackerMixin(viewsets.ViewSetMixin):

    @staticmethod
    def set_last_activity_timestamp(original_function):
        def wrapper(*args, **kwargs):
            original_result = original_function(*args, **kwargs)
            try:
                user = original_result.user
            except exceptions.InvalidToken:
                pass
            else:
                if str(user) != 'AnonymousUser':
                    user.last_activity = timezone.now()
                    user.save()
            return original_result
        return wrapper

    @set_last_activity_timestamp
    def initialize_request(self, request, *args, **kwargs):
        return super().initialize_request(request, *args, **kwargs)
