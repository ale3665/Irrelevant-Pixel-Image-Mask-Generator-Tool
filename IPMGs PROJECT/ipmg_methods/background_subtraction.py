import cv2
import numpy as np

def generate_background_mask(image_bgr):
    """
    Generate a background mask using color-based segmentation.
    Assumes the background has a distinguishable color distribution.

    Parameters:
    - image_bgr: np.ndarray (BGR image as expected by OpenCV)

    Returns:
    - mask: np.ndarray (binary mask of foreground objects)
    """
    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    # Define the color range for the background (adjust these ranges as needed)
    lower_background = np.array([0, 0, 0])        # Lower bound of background color in HSV
    upper_background = np.array([180, 255, 120])   # Upper bound of background color in HSV

    # Create a mask where the background pixels fall within the specified color range
    background_mask = cv2.inRange(hsv, lower_background, upper_background)

    # Invert the mask to get the foreground (objects)
    foreground_mask = cv2.bitwise_not(background_mask)

    return foreground_mask
