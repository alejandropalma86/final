from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Service


# class ServiceListView(View):
#     template_name = 'services/services.html'
#     def get(self, request):
#         services = Service.objects.all()
#         return render(request,self.template_name, dict(services=services))

class ServiceView(View):
    template_name = 'services/services.html'
    def get(self, request, service_id):
        service = get_object_or_404(Service, id=service_id)
        return render(request, self.template_name, dict(service=service))