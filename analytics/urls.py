from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('like', views.LikeView)

urlpatterns = router.urls
