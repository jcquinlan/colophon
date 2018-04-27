from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from core.models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # If a new instance of the User model was created, created
    # a UserProfile for that User
    print('POST SAVE SIGNAL EXECUTED')
    if created:
        UserProfile.objects.get_or_create(user=instance)
