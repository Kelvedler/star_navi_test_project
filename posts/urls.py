from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('post', views.PostCreateView)

urlpatterns = [
    path('post/<int:pk>/like', views.LikeView.as_view({'post': 'create'})),
    path('post/<int:pk>/unlike', views.LikeView.as_view({'delete': 'destroy'})),
]

urlpatterns += router.urls
