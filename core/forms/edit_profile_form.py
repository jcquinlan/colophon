import json
from django import forms
from core.models import UserProfile

class EditProfileForm(forms.ModelForm):
    profile_image = forms.CharField(widget=forms.HiddenInput(), required=False, label='')

    class Meta:
        model = UserProfile
        exclude = ['user']

    def save(self, request):
        profile = super(EditProfileForm, self).save(commit=False)
        profile.user = request.user
        profile.save()

        return profile

