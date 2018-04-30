from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404

from core.models import DesignDocument, DesignDocumentPackage, UserDocumentFavorite

class DesignDocumentDetailView(View):
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

    def delete(self, request, document_id):
        design_document = DesignDocument.objects.get(id=document_id)

        if design_document:
            design_document.delete()

            return JsonResponse({'message': 'Document deleted'}, status=204)
        else:
            return JsonResponse({'message': 'Document not found'}, status=404)


