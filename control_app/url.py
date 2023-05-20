from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeographicLocationViewSet

router = DefaultRouter()
router.register(r'geographiclocation', GeographicLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

