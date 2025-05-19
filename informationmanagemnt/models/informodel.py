from django.db import models


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
    created_at = models.DateField(auto_now=True)
