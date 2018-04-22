from django.views import View
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument, DesignDocumentPackage
from core.forms.edit_design_document_form import EditDesignDocumentForm

class DesignDocumentEditView(LoginRequiredMixin, View):
    template_name = 'core/design-documents/design-document-edit.html'

    def get(self, request, document_id):
        design_document = get_object_or_404(DesignDocument, id=document_id, uploaded_by=request.user)
        design_document_form = EditDesignDocumentForm(instance=design_document)
        document_package = None

        if design_document.has_download:
            document_package = DesignDocumentPackage.objects.get(design_document=design_document)

        context = {
            'document': design_document,
            'design_document_form': design_document_form,
            'document_package': document_package
        }

        return render(request, self.template_name, context)

    def post(self, request, document_id):
        design_document = get_object_or_404(DesignDocument, id=document_id, uploaded_by=request.user)
        design_document_form = EditDesignDocumentForm(request.POST, instance=design_document)
        document_package = None

        if design_document_form.is_valid():
            design_document_form.save(request)

            if design_document.has_download:
                document_package = DesignDocumentPackage \
                    .objects.get(design_document=design_document)

            # Redirect to the detail page, with message param for successful edit
            return redirect("%s?m=es" % reverse(
                'design_document_detail',
                args=(design_document.id,)
            ))

        context = {
            'document': design_document,
            'design_document_form': design_document_form,
            'document_package': document_package
        }

        return render(request, self.template_name, context)

