from django.views import View
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms.create_design_document_form import CreateDesignDocumentForm

from core.models import DesignDocument

class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'

    def get(self, request):
        design_documents = DesignDocument.objects.all(),
        form = CreateDesignDocumentForm()

        context = {
            'design_documents': design_documents,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateDesignDocumentForm(request.POST)

        if form.is_valid():
            form.save(request)

            redirect(reverse('dashboard'))

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
