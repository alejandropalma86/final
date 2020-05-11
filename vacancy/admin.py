from django.contrib import admin
from .models import JobVacancy

class JobVacancyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(JobVacancy, JobVacancyAdmin)


