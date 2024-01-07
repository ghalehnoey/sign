from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadImageForm
from .remove_background import remove_background
import io
from PIL import Image

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            output_image = remove_background(image)

            # Create an in-memory binary stream to store the image data
            image_stream = io.BytesIO()
            format_str = "PNG"  # You can change the format as needed (e.g., PNG, JPEG)
            output_pil_image = Image.fromarray(output_image)
            output_pil_image.save(image_stream, format=format_str)
            image_stream.seek(0)

            # Prepare the response to serve the image for download
            response = HttpResponse(image_stream, content_type="image/png")  # Adjust content type as needed
            response['Content-Disposition'] = 'attachment; filename=output_image.png'
            return response

    else:  # For GET requests or invalid form
        form = UploadImageForm()

    return render(request, 'my_app/upload_image.html', {'form': form})

def serve_image(request):
    if request.method == 'POST':
        # Process the image as needed
        # Assuming you have 'image_data' which is the processed image data

        # Sample data (replace this with your actual processed image data)
        image_data = b'Sample image data'

        # Create an in-memory binary stream to store the image data
        image_stream = io.BytesIO(image_data)
        format_str = "PNG"  # Change format if necessary (e.g., JPEG)
        
        # Save the processed image to the in-memory binary stream
        output_pil_image = Image.frombytes(data=image_data)  # Replace this line with your actual image creation logic

        # Save the image to the stream
        output_pil_image.save(image_stream, format=format_str)
        image_stream.seek(0)

        # Prepare the HTTP response to serve the image for download
        response = HttpResponse(image_stream, content_type=f"image/{format_str.lower()}")
        response['Content-Disposition'] = 'attachment; filename="processed_image.png"'  # Adjust filename and extension
        return response

    # Handle cases where it's not a POST request (optional)
    return HttpResponse("Invalid request")
