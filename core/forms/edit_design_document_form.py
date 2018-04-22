import json
from django import forms
from core.models import DesignDocument, DesignDocumentImage

class EditDesignDocumentForm(forms.ModelForm):
    document_images = forms.CharField(widget=forms.HiddenInput(), required=False, label='')
    asset_url = forms.CharField(widget=forms.HiddenInput(), required=False, label='')
    document_images_to_remove = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        label=''
    )
    asset_url_to_remove = forms.CharField(widget=forms.HiddenInput(), required=False, label='')

    class Meta:
        model = DesignDocument
        exclude = ['uploaded_by', 'created_at', 'has_download', 'has_assets',]

    def save(self, request):
        data = self.cleaned_data
        design_document = super(EditDesignDocumentForm, self).save(commit=False)

        # Mutably move the file urls from the cleaned data
        file_urls_string = data.pop('document_images')
        asset_url_string = data.pop('asset_url')
        document_images_to_remove_string = data.pop('document_images_to_remove')

        # When editing a file, these fields will be empty, since the values of the inputs
        # need to be manually set, as they are hidden. This means that editing a design_document
        # does not duplicate the fule_urls or asset_url over and over.
        file_urls = json.loads(file_urls_string) if file_urls_string else []
        asset_url = json.loads(asset_url_string) if asset_url_string else None

        document_images_to_remove = json.loads(document_images_to_remove_string) \
            if document_images_to_remove_string else []

        # Assign the user that created/edited the document
        design_document.uploaded_by = request.user

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

            design_document.images.add(design_document_image)

        for image_id in document_images_to_remove:
            design_document_images = DesignDocumentImage.objects.filter(
                id=image_id,
                design_document=design_document,
            )

            if design_document_images:
                design_document_images.delete()

        design_document.save()

        return design_document
