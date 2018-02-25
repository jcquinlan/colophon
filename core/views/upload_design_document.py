from django.views import View
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms.create_design_document_form import CreateDesignDocumentForm

from core.models import DesignDocument

class UploadDesignDocumentView(LoginRequiredMixin, View):
    template_name = 'core/upload-design-document.html'

    def get(self, request):
        form = CreateDesignDocumentForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateDesignDocumentForm(request.POST)

        if form.is_valid():
            form.save(request)

            return redirect(reverse('dashboard'))

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
