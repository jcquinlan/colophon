from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

class ChangePasswordView(PasswordChangeView):
    template_name = 'core/profile/change-password.html'
    success_url = reverse_lazy('profile')
