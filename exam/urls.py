from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.start_test, name='start_test'),
    path('test/<int:test_id>/submit/', views.submit_test, name='submit_test'),
    path('test/<int:test_id>/result/', views.result, name='result'),
]
