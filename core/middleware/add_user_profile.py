from django.utils.deprecation import MiddlewareMixin
from core.models import UserProfile

class AddUserProfileMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user

        if not user.is_anonymous:
            try:
                profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                profile = None

            request.user.profile = profile

        return None
