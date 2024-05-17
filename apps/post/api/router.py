from rest_framework.routers import DefaultRouter

from apps.post.api.views import PostModelViewSet

router = DefaultRouter()

router.register(prefix='', basename='post', viewset=PostModelViewSet)

urlpatterns = router.urls