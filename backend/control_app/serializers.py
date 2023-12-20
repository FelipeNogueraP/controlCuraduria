from rest_framework import serializers
from .models import LicenceHolderResponsible


class LicenceHolderResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenceHolderResponsible
        fields = "__all__"
