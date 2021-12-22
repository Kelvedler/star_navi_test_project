from django import urls
from django.views.decorators import csrf
from rest_framework_simplejwt import views as jwt_views
from . import views as user_views

urlpatterns = [
    urls.path('signup/', csrf.csrf_exempt(user_views.Signup.as_view())),
    urls.path('login/', jwt_views.TokenObtainPairView.as_view())
]
