from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from raterapi.views import CategoryViewSet, GameImageViewSet, GameRatingViewSet, GameReviewViewSet, GameViewSet, login_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'game-images', GameImageViewSet, basename='game-image')
router.register(r'game-ratings', GameRatingViewSet, basename='game-rating')
router.register(r'game-reviews', GameReviewViewSet, basename='game-review')
router.register(r'games', GameViewSet, basename='game')

urlpatterns = [
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
    path('admin/', admin.site.urls),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

