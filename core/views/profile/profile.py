from django.views import View
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument

class ProfileView(LoginRequiredMixin, View):
    template_name = 'core/profile/profile.html'

    def get(self, request):
        design_documents = DesignDocument.objects.filter(uploaded_by=request.user)

        context = {
            'documents': design_documents
        }

        return render(request, self.template_name, context)
