from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import viewsets
from .models import LicenceHolderResponsible

from .serializers import LicenceHolderResponsibleSerializer

class LicenceHolderResponsibleViewSet(viewsets.ModelViewSet):
    queryset = LicenceHolderResponsible.objects.all()
    serializer_class = LicenceHolderResponsibleSerializer
