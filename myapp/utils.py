# import uuid
# from PIL import Image
# import pytesseract
# import PyPDF2
# from .models import UploadedFile

# def handle_uploaded_file(file):
#     # Generate a GUID for the file name
#     guid = str(uuid.uuid4())
#     file_extension = file.name.split('.')[-1]
#     new_filename = f"{guid}.{file_extension}"
    
#     # Save the file
#     uploaded_file = UploadedFile(file=file, file_name=new_filename)
#     uploaded_file.save()
    
#     return uploaded_file

# def extract_text_from_file(file_path):
#     text = ""
#     if file_path.endswith('.pdf'):
#         with open(file_path, "rb") as file:
#             reader = PyPDF2.PdfFileReader(file)
#             for page_num in range(reader.numPages):
#                 page = reader.getPage(page_num)
#                 text += page.extract_text()
#     else:
#         # Assuming it's an image file
#         image = Image.open(file_path)
#         text = pytesseract.image_to_string(image)
    
#     return text