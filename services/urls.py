from django.urls import path
from .views import ServiceView

urlpatterns = [
    #Patshs del Core
    path('', ServiceView.as_view(), name='services'),
   
]
