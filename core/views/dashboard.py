from django.views import View
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms.create_design_document_form import CreateDesignDocumentForm

from core.models import DesignDocument

class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'

    def get(self, request):
        documents = DesignDocument.objects.all()

        context = {
            'documents': documents,
        }

        return render(request, self.template_name, context)
