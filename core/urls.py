from django.urls import path
from . import views
from .views import HomeView, AboutView, AddressView

urlpatterns = [
    #Patshs del Core
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('address/', AddressView.as_view(), name='address'),
    
]
