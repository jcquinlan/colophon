from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument, UserDocumentDownload, UserDocumentFavorite

class ProfileView(LoginRequiredMixin, View):
    template_name = 'core/profile/profile.html'

    def get(self, request):
        filter_param = request.GET.get('filter')

        design_documents = self.get_filtered_documents(filter_param, request.user) if \
            filter_param else \
            DesignDocument.objects.filter(uploaded_by=request.user)

        print(design_documents)

        context = {
            'documents': design_documents,
            'filter_param': filter_param
        }

        return render(request, self.template_name, context)

    def delete(self, request):
        request.user.delete()

        return JsonResponse({'message': 'Account successfully deleted'}, status=200)

    def get_filtered_documents(self, filter_param, user):
        try:
            model_class = {
                'favorites': UserDocumentFavorite,
                'downloads': UserDocumentDownload
            }[filter_param]

            return [item.design_document for item in model_class.objects.filter(user=user)]
        except KeyError:
            return DesignDocument.objects.filter(uploaded_by=user)

