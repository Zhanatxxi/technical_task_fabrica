from django.db.models.signals import post_save
from django.dispatch import receiver

from src.account.models import CustomUser, UserProfile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.__dict__.get('profile'):
            profile = UserProfile(
                user_id=instance
            )
            profile.generate_telegram_token()
            profile.save()
