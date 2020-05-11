from django.urls import path
from . import views
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('iniciar_sesion', LoginView.as_view(), name ='login'),
    path('cerrar_sesion', LogoutView.as_view(), name ='logout'),
    path('registro', RegisterView.as_view(), name ='register'),
    
]

    