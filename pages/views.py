from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Page

class PageView(View):
    template_name = 'pages/sample.html'
    def get(self, request, page_id):
        page = get_object_or_404(Page, id=page_id)
        return render(request, self.template_name, dict(page=page))



