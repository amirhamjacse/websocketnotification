from informationmanagemnt.models import InformationData
from informationmanagemnt.serializers import InforamtionDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InformationDataView(APIView):
    model = InformationData

    def get(self, request):
        query = InformationData.objects.all()
        serialized = InforamtionDataSerializer(query, many=True)
        return Response(data=serialized.data)