from django.views import View
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument

class DesignDocumentDetailView(LoginRequiredMixin, View):
    template_name = 'core/design-documents/design-document-detail.html'

    def get(self, request, document_id):
        design_document = get_object_or_404(DesignDocument, id=document_id)

        context = {
            'design_document': design_document
        }

        return render(request, self.template_name, context)
