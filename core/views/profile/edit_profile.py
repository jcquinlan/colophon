from django.views import View
from django.http import JsonResponse
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
        is_adding_profile_image = request.GET.get('action') == 'profile_image'

        if is_adding_profile_image:
            return self.save_profile_image(request)
        else:
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

    def save_profile_image(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        image_url = request.POST.get('profile_image_url')

        print(request.POST)

        if not image_url:
            return JsonResponse({'message': 'No image URL found'}, status=400)
        else:
            user_profile.profile_image = image_url
            user_profile.save()

            return JsonResponse({'message': 'It worked'}, status=200)
