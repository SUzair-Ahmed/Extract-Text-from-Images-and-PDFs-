from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.conf import settings
import pytesseract
from PIL import Image
import pdfplumber
from pdf2image import convert_from_path
from .models import UploadedFile
from .forms import FileUploadForm

User = get_user_model()

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('login') 

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    if images:
        image_path = pdf_path.replace('.pdf', '.png')
        images[0].save(image_path, 'PNG')
        return image_path
    return None

@login_required
def home(request):
    uploaded_file_url = None
    extracted_text = None
    is_pdf = False
    preview_image_url = None

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save()
            file_path = uploaded_file_instance.file.path
            file_name = uploaded_file_instance.file.name

            if file_name.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(file_path)
                is_pdf = True
                preview_image_path = convert_pdf_to_image(file_path)
                if preview_image_path:
                    preview_image_url = preview_image_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)
            else:
                extracted_text = extract_text_from_image(file_path)
                preview_image_url = uploaded_file_instance.file.url

            uploaded_file_instance.extracted_text = extracted_text
            uploaded_file_instance.save()

            uploaded_file_url = uploaded_file_instance.file.url
    else:
        form = FileUploadForm()

    return render(request, 'home.html', {
        'form': form,
        'uploaded_file_url': uploaded_file_url,
        'extracted_text': extracted_text,
        'is_pdf': is_pdf,
        'preview_image_url': preview_image_url,
    })
