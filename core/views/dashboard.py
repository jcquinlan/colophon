from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms.create_design_document_form import CreateDesignDocumentForm

from core.models import DesignDocument

class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'

    def get(self, request):
        all_documents = DesignDocument.objects.all().order_by('-created_at')
        paginator = Paginator(all_documents, 10)

        page = request.GET.get('page')

        documents = paginator.get_page(page)

        context = {
            'documents': documents,
        }

        return render(request, self.template_name, context)
