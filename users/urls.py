from django import urls
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views as user_views

urlpatterns = [
    urls.path('signup/', user_views.Signup.as_view()),
    urls.path('login/', jwt_views.TokenObtainPairView.as_view())
]

router = routers.SimpleRouter()
router.register('activity', user_views.Activity)

urlpatterns += router.urls
