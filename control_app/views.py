from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import viewsets
from .models import GeographicLocation

from .serializers import GeographicLocationSerializer


@method_decorator(csrf_exempt, name="dispatch")
class ExemptCSRFSessionAuthentication(auth_views.LoginView):
    pass

class GeographicLocationViewSet(viewsets.ModelViewSet):
    queryset = GeographicLocation.objects.all()
    serializer_class = GeographicLocationSerializer
