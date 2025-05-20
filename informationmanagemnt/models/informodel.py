from django.db import models
from django.contrib.auth.models import User


class InformationData(models.Model):
    name = models.CharField(
        max_length=50, null=True,
        blank=True
    )
    f_name = models.CharField(
        max_length=50, null=True,
        blank=True
    )
    m_name = models.CharField(
        max_length=50, null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        User, related_name='created_info', on_delete=models.CASCADE
    )
    current_approver = models.ForeignKey(
        User, related_name='to_approve',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ], default='PENDING')
    current_level = models.IntegerField(default=1)
    current_group = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class ApprovalLog(models.Model):
    info = models.ForeignKey(InformationData, on_delete=models.CASCADE, related_name='logs')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.CharField(max_length=100)
    action = models.CharField(max_length=10, choices=[('APPROVED', 'Approved'), ('REJECTED', 'Rejected')])
    timestamp = models.DateTimeField(auto_now_add=True)