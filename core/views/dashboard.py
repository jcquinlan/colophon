from django.views import View
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument

class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'

    def get(self, request):
        design_documents = DesignDocument.objects.all()

        context = {
            'design_documents': design_documents
        }

        return render(request, self.template_name, context)
