from rest_framework import serializers
from .models import GeographicLocation


class GeographicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicLocation
    fields = "__all__"
