from django.views import View
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument, DesignDocumentPackage

class DesignDocumentDetailView(LoginRequiredMixin, View):
    template_name = 'core/design-documents/design-document-detail.html'

    def get(self, request, document_id):
        design_document = get_object_or_404(DesignDocument, id=document_id)
        document_package = None

        if design_document.has_download:
            document_package = DesignDocumentPackage.objects.get(design_document=design_document)

        context = {
            'document': design_document,
            'document_package': document_package
        }

        return render(request, self.template_name, context)
