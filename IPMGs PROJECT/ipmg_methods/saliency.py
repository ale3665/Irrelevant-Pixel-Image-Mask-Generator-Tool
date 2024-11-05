import cv2
import numpy as np


def generate_saliency_mask(image_bgr):
    """
    Generate a saliency mask using OpenCV's StaticSaliencySpectralResidual method.

    Parameters:
    - image_bgr: np.ndarray (BGR image as expected by OpenCV)

    Returns:
    - saliency_mask: np.ndarray (saliency mask with values scaled to 0-255)
    """
    # Create the saliency detector
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()

    # Compute the saliency map
    success, saliency_map = saliency.computeSaliency(image_bgr)

    # Scale saliency map to 0-255 for display purposes
    saliency_mask = (saliency_map * 255).astype("uint8")

    return saliency_mask
