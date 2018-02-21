from django import forms
from core.models import DesignDocument

class CreateDesignDocumentForm(forms.ModelForm):
    class Meta:
        model = DesignDocument
        exclude = ['uploaded_by', 'created_at', 'has_download', 'has_assets',]

    def save(self, request):
        data = self.cleaned_data
        design_document = DesignDocument(
            **data,
            uploaded_by=request.user,
        )

        design_document.save()
