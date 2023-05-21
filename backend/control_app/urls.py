from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import GeographicLocationViewSet

router = DefaultRouter()
router.register(r'geographiclocation', GeographicLocationViewSet)

urlpatterns = [
    path('auth/login', auth_views.LoginView.as_view(), name='login'),
    path('auth/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]

