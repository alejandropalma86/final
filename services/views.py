from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Service


class ServiceListView(ListView):
    template_name = 'services/services_list.html'
    queryset = Service.objects.all()


class ServiceDetailView(View):
    template_name = 'services/services_detail.html'
    def get(self, request, service_id):
        service = get_object_or_404(Service, id=service_id)
        return render(request, self.template_name, dict(service=service))