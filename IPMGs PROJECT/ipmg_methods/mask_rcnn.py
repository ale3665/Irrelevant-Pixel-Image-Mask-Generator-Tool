from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import numpy as np

# Load the processor and model once to save loading time
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", ignore_mismatched_sizes=True)

def generate_mask_rcnn_mask(image_pil):
    """
    Generate an object detection mask using the Mask R-CNN model.

    Parameters:
    - image_pil: PIL.Image (the input image in PIL format)

    Returns:
    - mask: np.ndarray (binary mask for detected objects)
    """
    # Process the PIL image
    inputs = processor(images=image_pil, return_tensors="pt")
    
    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Post-process the outputs to obtain detection boxes
    target_sizes = torch.tensor([image_pil.size[::-1]])  # Image size in (height, width)
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.5)[0]
    
    # Create a blank mask for detected objects
    mask = np.zeros((image_pil.height, image_pil.width), dtype=np.uint8)
    
    # Fill bounding boxes on the mask for each detected object
    for box in results["boxes"]:
        x_min, y_min, x_max, y_max = map(int, box)
        mask[y_min:y_max, x_min:x_max] = 255  # Fill detected areas with white (255)
    
    return mask
