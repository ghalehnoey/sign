from django.urls import path
from . import views

urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    # Assuming serve_image is defined in views.py
    path('serve_image/', views.serve_image, name='serve_image'),  # Add this line for serving the processed image
]
