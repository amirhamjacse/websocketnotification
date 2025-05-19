from informationmanagemnt.models import InformationData
from rest_framework import serializers, viewsets


class InforamtionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationData
        fields = [
            'id',
            'name',
            'f_name',
            'm_name'
        ]
