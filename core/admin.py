from django.contrib import admin
from core.models import DesignDocument, DesignDocumentImage, DesignDocumentPackage

# Register your models here.
admin.site.register(DesignDocument)
admin.site.register(DesignDocumentImage)
admin.site.register(DesignDocumentPackage)
