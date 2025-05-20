from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from informationmanagemnt.models import InformationData, ApprovalLog
from informationmanagemnt.serializers import InformationsDataSerializer
from informationmanagemnt.utils import get_group_by_level, user_in_group
from django.contrib.auth.models import Group


class CreateInformationView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InformationsDataSerializer(data=request.data)
        if serializer.is_valid():
            info = serializer.save(created_by=request.user)

            group_name = get_group_by_level(1)
            group = Group.objects.filter(name=group_name).first()
            first_approver = group.user_set.first() if group else None

            info.current_group = group_name
            info.current_approver = first_approver
            info.save()
            return Response({"message": "Submitted for approval"})
        return Response(serializer.errors, status=400)


class ApproveInformationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        info = get_object_or_404(InformationData, pk=pk)

        if not user_in_group(request.user, info.current_group):
            return Response({"detail": "You are not authorized for this level"}, status=403)

        # Log approval
        ApprovalLog.objects.create(
            info=info, user=request.user,
            group=info.current_group, action='APPROVED'
        )

        next_level = info.current_level + 1
        next_group_name = get_group_by_level(next_level)

        if next_group_name:
            next_group = Group.objects.filter(name=next_group_name).first()
            next_user = next_group.user_set.first()
            info.current_group = next_group_name
            info.current_level = next_level
            info.current_approver = next_user
        else:
            info.status = 'APPROVED'
            info.current_group = None
            info.current_approver = None

        info.save()
        return Response({"message": "Approved"})


class RejectInformationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        info = get_object_or_404(InformationData, pk=pk)

        if not user_in_group(request.user, info.current_group):
            return Response({"detail": "You are not authorized to reject"}, status=403)

        ApprovalLog.objects.create(
            info=info, user=request.user,
            group=info.current_group, action='REJECTED'
        )

        info.status = 'REJECTED'
        info.current_group = None
        info.current_approver = None
        info.save()

        return Response({"message": "Rejected"})
