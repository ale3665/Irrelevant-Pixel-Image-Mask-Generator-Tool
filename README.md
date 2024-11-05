# Irrelevant-Pixel-Image-Mask-Generator-Tool
Research Project about Irrelevant Pixel Image-Mask Generator Tool.

# Irrelevant Pixel Mask Generator (IPMGs)

This project generates various types of masks on input images using different image processing techniques. It includes techniques like **Saliency Map**, **Background Subtraction**, **Edge Detection**, **Mask R-CNN**, and **DeepLabV3** to highlight or remove irrelevant pixel areas in an image. The application is built with **Streamlit** and supports easy setup using a virtual environment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Makefile](#makefile)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+
- Recommended to use a virtual environment

### Step-by-Step Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    ```

    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

The application will open in a new browser tab, displaying the interface for uploading images and applying different mask generation techniques.

## Usage

1. **Upload an Image**: Click "Choose an image..." to upload a JPEG or PNG file.
2. **Select a Technique**: Choose a masking technique from the dropdown.
3. **Generate Mask**: The selected mask will be generated and displayed on the page.

## Features

This project supports several image processing techniques for generating masks. Below is a summary of each technique:

### 1. Saliency Map
Generates a saliency mask using OpenCV's `StaticSaliencySpectralResidual` method to highlight prominent regions in the image.

### 2. Background Subtraction
Uses color-based segmentation in HSV color space to separate foreground and background elements.

### 3. Edge Detection
Generates a mask of image edges using the Canny edge detection algorithm.

### 4. Mask R-CNN (DETR Model)
Uses the DETR (DEtection TRansformer) model from Hugging Face’s `transformers` library to generate bounding box masks for detected objects.

### 5. DeepLabV3 (Segmentation)
Applies semantic segmentation to the image using the DeepLabV3 model with the `Segformer` processor, highlighting different classes in the image.

## Makefile

For macOS/Linux users, a `Makefile` is included to simplify setup, installation, and running. 

### Available Commands

- **Install dependencies and run the app**:
    ```bash
    make
    ```

- **Only install dependencies**:
    ```bash
    make install
    ```

- **Run the app without reinstalling dependencies**:
    ```bash
    make run
    ```

- **Clean up the virtual environment and cache**:
    ```bash
    make clean
    ```

For Windows users, the Makefile might not work directly. Instead, a `setup.bat` or `setup.ps1` script can be used for setup and running.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements, report bugs, or add new features.

### Steps to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/YourFeature`)
3. **Commit your changes** (`git commit -m 'Add a new feature'`)
4. **Push to the branch** (`git push origin feature/YourFeature`)
5. **Create a new Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
