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

    def post(self, request):
        serialized = InforamtionDataSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
        return Response(data=serialized.data)
    
    def patch(self, request):
        instance = InformationData.objects.filter(pk=1).last()
        serialize = InforamtionDataSerializer(
            instance, data=request.data,
            partial=True
            )
        if serialize.is_valid():
            serialize.save()
        # print(instance.id, 12* '-----------')
        return Response(data=serialize.data)

    def delete(self, request):
        instance = InformationData.objects.filter(pk=2).last()
        instance.delete()
        return Response({"details": "Delete Successfully"})
