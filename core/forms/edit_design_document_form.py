import json
from django import forms
from core.models import DesignDocument, DesignDocumentImage, DesignDocumentPackage

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

    def is_valid(self):
        valid = super(EditDesignDocumentForm, self).is_valid()

        if not valid:
            return valid

        design_document = self.instance
        removing_too_many_images = False
        trying_to_remove_asset = False

        document_images_to_remove = self.pull_and_parse_attr('document_images_to_remove', [])
        asset_url = self.pull_and_parse_attr('asset_url', None)
        asset_url_to_remove = self.pull_and_parse_attr('asset_url_to_remove', None)

        # If the user is trying to remove all their images
        if len(document_images_to_remove) >= len(design_document.images.all()):
            removing_too_many_images = True
            self.add_error(None, 'You must leave at least one image.')

        # If the user is trying to remove an asset without also providing one
        if asset_url_to_remove and not asset_url:
            trying_to_remove_asset = True
            self.add_error(None, 'You cannot remove an asset without providing a new one.')

        if removing_too_many_images or trying_to_remove_asset:
            return False

        return valid

    def save(self, request):
        data = self.cleaned_data
        design_document = super(EditDesignDocumentForm, self).save(commit=False)

        # Mutably move the file urls from the cleaned data
        file_urls = self.pull_and_parse_attr('document_images', [])
        asset_url = self.pull_and_parse_attr('asset_url', None)
        document_images_to_remove = self.pull_and_parse_attr('document_images_to_remove', [])

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

    def pull_and_parse_attr(self, attr_name, default):
        """Pulls an attribute from the uncleaned data and parses it into a useable value"""
        string_val = self.data.get(attr_name)
        return json.loads(string_val) if string_val else default
