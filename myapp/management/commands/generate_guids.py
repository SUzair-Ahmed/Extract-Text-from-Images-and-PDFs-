from django.core.management.base import BaseCommand
from myapp.models import UserSocialAuth
import uuid

class Command(BaseCommand):
    help = 'Generate GUIDs for existing user social auth records'

    def handle(self, *args, **kwargs):
        users = UserSocialAuth.objects.all()
        for user in users:
            if not user.guid:  # Only update if GUID is not set
                user.guid = uuid.uuid4()
                user.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated GUIDs for all user social auth records'))
