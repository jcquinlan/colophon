from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from core.models import DesignDocument, UserDocumentFavorite

class DesignDocumentFavoriteView(LoginRequiredMixin, View):
    def post(self, request, document_id):
        design_document = DesignDocument.objects.get(id=document_id)

        if design_document:
            try:
                favorite = UserDocumentFavorite.objects.get(
                    user=request.user,
                    design_document=design_document
                )

                favorite.delete()

                return JsonResponse({
                    'message': 'Document unfavorited',
                    'favorited': False
                }, status=200)

            except ObjectDoesNotExist:
                new_favorite = UserDocumentFavorite(
                    user=request.user,
                    design_document=design_document
                )
                new_favorite.save()

                return JsonResponse({
                    'message': 'Document favorited',
                    'favorited': True
                }, status=200)
        else:
            return JsonResponse({'message': 'Missing document'}, status=404)
