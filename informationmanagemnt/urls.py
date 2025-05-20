
from django.urls import path
from informationmanagemnt import views
from informationmanagemnt.views import (
    CreateInformationView, ApproveInformationView, RejectInformationView,

)

urlpatterns = [
    path('info/', views.InformationDataView.as_view(), name='info_page'),
    path('info/create/', CreateInformationView.as_view()),
    path('info/<int:pk>/approve/', ApproveInformationView.as_view()),
    path('info/<int:pk>/reject/', RejectInformationView.as_view()),
]
