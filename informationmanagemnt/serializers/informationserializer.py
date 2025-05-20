from informationmanagemnt.models import (
    InformationData, ApprovalLog
)
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


class InformationsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationData
        fields = '__all__'
        read_only_fields = ['created_by', 'status', 'current_level', 'current_group', 'current_approver']

class ApprovalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalLog
        fields = '__all__'