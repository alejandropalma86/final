from django.urls import path
from .views import ServiceView

urlpatterns = [
    #path('', ServiceListView.as_view(), name='services_list'),
    path('<int:service_id>/', ServiceView.as_view(), name='services')
]
