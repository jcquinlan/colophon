from django.views import View
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import DesignDocument

class ProfileView(LoginRequiredMixin, View):
    template_name = 'core/profile/profile.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
