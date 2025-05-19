
from django.urls import path
from informationmanagemnt import views

urlpatterns = [
    path('info/', views.InformationDataView.as_view(), name='info_page')
]
