from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class ConfirmDeleteAccountView(LoginRequiredMixin, View):
    template_name = 'core/profile/confirm-delete-account.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
