from django.urls import path
from . import views
from .views import JobVacancyView

urlpatterns = [
    path('', JobVacancyView.as_view(), name='vacancy'),
]