from django.shortcuts import render
from django.views import View
from .models import JobVacancy

class JobVacancyView(View):
    def get(self, request):
        template_name = 'vacancy/vacancy.html'
        context = dict(
        vacancies = JobVacancy.objects.all(), 
        )
        return render(request, template_name, context)
