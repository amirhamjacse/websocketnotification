from django.contrib import admin
from informationmanagemnt.models import InformationData
# Register your models here.
@admin.register(InformationData)

class InformationDataAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )