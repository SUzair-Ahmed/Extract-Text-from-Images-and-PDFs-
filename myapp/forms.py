# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('username', 'email')

# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Replace with your custom user model if applicable
from .models import UploadedFile

class CustomUserCreationForm(UserCreationForm):
    # Add any additional fields or customization here if needed
    class Meta:
        model = CustomUser  # Replace with your custom user model if applicable
        fields = ('username', 'password1', 'password2')  # Example fields; adjust as necessary


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
