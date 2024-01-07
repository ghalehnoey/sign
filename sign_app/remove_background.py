import cv2
import numpy as np
from io import BytesIO
from PIL import Image

def remove_background(image_file):
    # Read the image file using PIL
    image = Image.open(image_file)
    image = np.array(image)  # Convert PIL image to NumPy array

    # Convert image to RGBA if not already in that format
    if image.shape[2] == 3:  # If image is RGB
        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)  # Convert to RGBA

    # Define threshold values
    white_threshold = 140  # White threshold
    threshold_value = 255  # Threshold value
    alpha_value = 190  # Adjusted alpha value for less transparency

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)

    # Apply thresholding to remove white background
    _, mask = cv2.threshold(gray_image, white_threshold, threshold_value, cv2.THRESH_BINARY)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Create signature without background (black with reduced transparency)
    signature_without_background = np.zeros(image.shape, dtype=np.uint8)
    signature_without_background[mask != 0] = (0, 0, 0, alpha_value)  # Black color with adjusted alpha

    return signature_without_background
