import json
from django import forms
from core.models import DesignDocument, DesignDocumentImage, DesignDocumentPackage

class CreateDesignDocumentForm(forms.ModelForm):
    document_images = forms.CharField(widget=forms.HiddenInput(), required=False, label='')
    asset_url = forms.CharField(widget=forms.HiddenInput(), required=False, label='')

    class Meta:
        model = DesignDocument
        exclude = ['uploaded_by', 'created_at', 'has_download', 'has_assets', 'weights']

    def is_valid(self):
        valid = super(CreateDesignDocumentForm, self).is_valid()
        missing_images = False
        missing_asset = False

        if not valid:
            return valid

        images = self.data['document_images']
        asset_url = self.data['asset_url']

        if not len(images):
            missing_images = True
            self.add_error(None, 'At least one image is required.')

        if not len(asset_url):
            missing_asset = True
            self.add_error(None, 'An InDesign or zip file of the document is required.')

        if missing_asset or missing_images:
            return False

        return valid


    def save(self, request):
        data = self.cleaned_data
        # Mutably move the file urls from the cleaned data
        file_urls_string = data.pop('document_images')
        asset_url_string = data.pop('asset_url')
        file_urls = json.loads(file_urls_string) if file_urls_string else []
        asset_url = json.loads(asset_url_string) if asset_url_string else None

        design_document = DesignDocument(
            **data,
            uploaded_by=request.user,
        )

        design_document.save()

        # Save document package if available
        if asset_url:
            design_document_package = DesignDocumentPackage(
                design_document=design_document,
                package_url=asset_url
            )

            design_document.has_download = True

            design_document.save()

            design_document_package.save()

        # Save document images if available
        for url in file_urls:
            design_document_image = DesignDocumentImage(
                design_document=design_document,
                image_url=url,
            )

            design_document_image.save()

            print(design_document_image)

            design_document.images.add(design_document_image)
