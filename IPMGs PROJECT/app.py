import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Import the mask generation functions from your IPMG methods
from ipmg_methods.saliency import generate_saliency_mask
from ipmg_methods.background_subtraction import generate_background_mask
from ipmg_methods.edge_detection import generate_edge_mask
from ipmg_methods.mask_rcnn import generate_mask_rcnn_mask
from ipmg_methods.deeplabv3 import generate_deeplabv3_mask

# Mapping techniques to their functions
techniques = {
    "Saliency Map": generate_saliency_mask,
    "Background Subtraction": generate_background_mask,
    "Edge Detection": generate_edge_mask,
    "Mask R-CNN": generate_mask_rcnn_mask,
    "DeepLabV3": generate_deeplabv3_mask
}

# Streamlit app setup
st.title("Irrelevant Pixel Mask Generator")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    # Open the image with PIL
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the PIL image to an OpenCV-compatible format (BGR) for non-deep-learning techniques
    image_np = np.array(image)  # Convert to a NumPy array (RGB format)
    
    # Check if the image has an alpha channel and remove it if present
    if image_np.shape[2] == 4:
        image_np = image_np[:, :, :3]  # Remove the alpha channel

    # Convert RGB image to BGR format for OpenCV
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Technique selection
    selected_technique = st.selectbox("Select a masking technique:", list(techniques.keys()))
    mask_function = techniques[selected_technique]

    # Generate and display the mask based on the selected technique
    st.write(f"Generating mask using {selected_technique}...")
    try:
        if selected_technique == "Mask R-CNN" or selected_technique == "DeepLabV3":
            # Pass the original PIL image for Mask R-CNN and DeepLabV3
            mask = mask_function(image)
        else:
            # Pass the OpenCV-compatible BGR image for other techniques
            mask = mask_function(image_bgr)
        
        st.image(mask, caption="Generated Mask", use_column_width=True)
    except Exception as e:
        st.error(f"An error occurred while generating the mask: {e}")
