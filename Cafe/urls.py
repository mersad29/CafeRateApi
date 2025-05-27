# URLs (urls.py)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Cafe.views import CafeViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'cafes', CafeViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]