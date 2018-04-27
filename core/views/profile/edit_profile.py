from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms.edit_profile_form import EditProfileForm
from core.models import UserProfile

class EditProfileView(LoginRequiredMixin, View):
    template_name = 'core/profile/edit-profile.html'

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None

        edit_profile_form = EditProfileForm(instance=user_profile)

        context = {
            'edit_profile_form': edit_profile_form
        }

        return render(request, self.template_name, context)


    def post(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None

        edit_profile_form = EditProfileForm(request.POST, instance=user_profile)

        if edit_profile_form.is_valid():
            edit_profile_form.save(request)

            return redirect(reverse('profile'))

        context = {
            'edit_profile_form': edit_profile_form
        }

        return render(request, self.template_name, context)


