from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import LicenceHolderResponsibleViewSet

router = DefaultRouter()
router.register(r'licenceholderresponsible', LicenceHolderResponsibleViewSet)

urlpatterns = [
    path('auth/login', auth_views.LoginView.as_view(), name='login'),
    path('auth/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]

