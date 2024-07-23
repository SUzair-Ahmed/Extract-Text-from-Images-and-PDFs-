import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.contrib.auth.models import User  # Import the User model
from django.conf import settings  # Import settings to reference the custom user model
from uuid import uuid4

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)



class UserSocialAuth(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    uid = models.CharField(max_length=255)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Ensure default value is set

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = uuid.uuid4()
        super(UserSocialAuth, self).save(*args, **kwargs)


def upload_to(instance, filename):
    ext = filename.split('.')[-1]                                                                    
    new_filename = f'{uuid.uuid4()}.{ext}'
    return f'uploads/{new_filename}'

class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to)
    # extracted_text = models.TextField(blank=True, null=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name