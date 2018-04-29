import json
from django import forms
from core.models import UserProfile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'profile_image']

    def save(self, request):
        profile = super(EditProfileForm, self).save(commit=False)
        profile.user = request.user
        profile.save()

        return profile

