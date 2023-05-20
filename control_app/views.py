from django.shortcuts import render
from rest_framework import viewsets
from .models import GeographicLocation
from .serializers import GeographicLocationSerializer


class GeographicLocationViewSet(viewsets.ModelViewSet):
    queryset = GeographicLocation.objects.all()
    serializer_class = GeographicLocationSerializer
