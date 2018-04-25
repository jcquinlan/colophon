from django.db import models
from django.contrib.auth.models import User
from core.models import DesignDocument

class DesignDocumentImage(models.Model):
    design_document = models.ForeignKey(DesignDocument, related_name="images", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=256)
    uploaded_at = models.DateTimeField(auto_now_add=True)