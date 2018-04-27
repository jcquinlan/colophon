from django.contrib import admin
from core.models import DesignDocument, DesignDocumentImage, DesignDocumentPackage, UserProfile

# Register your models here.
admin.site.register(DesignDocument)
admin.site.register(DesignDocumentImage)
admin.site.register(DesignDocumentPackage)
admin.site.register(UserProfile)
