from django.core.management.base import BaseCommand
from myapp.models import UserSocialAuth
import uuid

class Command(BaseCommand):
    help = 'Update existing UserSocialAuth records with GUIDs'

    def handle(self, *args, **kwargs):
        records = UserSocialAuth.objects.filter(guid__isnull=True)  # Filter records without GUIDs
        for record in records:
            record.guid = uuid.uuid4()
            record.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated GUIDs for existing records'))
