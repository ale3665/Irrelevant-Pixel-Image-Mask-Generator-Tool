import cv2

def generate_edge_mask(image_bgr):
    """
    Generate an edge detection mask using OpenCV's Canny edge detector.

    Parameters:
    - image_bgr: np.ndarray (BGR image as expected by OpenCV)

    Returns:
    - edges: np.ndarray (binary mask of edges)
    """
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges
