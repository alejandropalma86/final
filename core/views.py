from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
#def home(request):
    #return render(request,'core/home.html')
    template_name = 'core/home.html'


class AboutView(TemplateView):
# def about(request):
#     return render(request,'core/about.html')
    template_name = 'core/about.html'

class AddressView(TemplateView):
# def store(request):
#     return render(request,'core/store.html')
    template_name = 'core/address.html'




