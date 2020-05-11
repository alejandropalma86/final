from django.shortcuts import render
from django.views import View
from .models import Service


class ServiceView(View):
    template_name = 'services/services.html'
    def get(self, request):
        services = Service.objects.all()
        return render(request,self.template_name, dict(services=services))