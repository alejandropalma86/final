from django.urls import path
from .views import ServiceDetailView, ServiceListView

urlpatterns = [
    path('', ServiceListView.as_view(), name='services_list'),
    path('<int:service_id>/', ServiceDetailView.as_view(), name='services_detail')
]
