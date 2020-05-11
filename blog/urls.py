from django.urls import path
from . import views
from .views import BlogView, TagView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tagged"),
]