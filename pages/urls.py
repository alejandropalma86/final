from django.urls import path
from .views import PageView

urlpatterns = [
    path('<int:page_id>/', PageView.as_view(), name='page')
]