from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
import torch
import numpy as np
from PIL import Image

# Load the processor and model once to reduce loading time
processor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

def generate_deeplabv3_mask(image_pil):
    """
    Generate a semantic segmentation mask using the DeepLabV3 model.

    Parameters:
    - image_pil: PIL.Image (the input image in PIL format)

    Returns:
    - segmentation_mask: np.ndarray (segmentation mask with each class labeled by a unique integer)
    """
    # Process the PIL image with the processor
    inputs = processor(images=image_pil, return_tensors="pt")

    # Perform inference with the model
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the logits and compute the segmentation mask
    logits = outputs.logits[0]  # Get the first batch's logits
    segmentation_mask = torch.argmax(logits, dim=0).numpy()  # Find the most likely class for each pixel

    # Scale the segmentation mask for visualization
    scaled_mask = (segmentation_mask * (255 / segmentation_mask.max())).astype("uint8")

    return scaled_mask
