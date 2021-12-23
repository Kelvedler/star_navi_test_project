from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('post', views.PostCreateView)

urlpatterns = [
    path('post/<int:post_id>/like/', views.LikeView.as_view({'post': 'create'})),
    path('post/<int:post_id>/unlike/', views.LikeView.as_view({'delete': 'destroy'})),
]

urlpatterns += router.urls
