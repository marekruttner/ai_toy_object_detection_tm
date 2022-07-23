import cv2
from PIL import Image
import sys

width = 800
height = 480

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create the in-memory stream
def get_image_stream():
    while cap.is_open():
        success, image = cap.read()
        if not success:
            sys.exit(
                "Error: Failed to read from camera"
            )
    image = Image.open(stream)
    return image