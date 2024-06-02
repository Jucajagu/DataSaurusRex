from PIL import Image
import cv2
import numpy as np
import base64
import numpy as np
import pickle

def transform_image(image, target_size=(150, 150)):
    """Las imágenes original se transforman para que cada una de estas tenga el mismo número de canales y dimensiones. La imagen en img_path se convierte en una de formato RGB

    Args:
        img: la imagen abierta a transformar
        target_size (tuple, optional): Dimensiones objetivo con las que se estandarizan todas las imágenes. Defaults to (150, 150).

    Returns:
        array: imagen convertida a array y en RGB
    """
    with Image.open(image) as img:
        img = img.resize(target_size)
        img_array = np.asarray(img)
        
        # Ensure image has 3 channels
        if img_array.ndim == 2:  # Grayscale image
            img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
        elif img_array.ndim == 3 and img_array.shape[2] == 4:  # RGBA image
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
        elif img_array.ndim == 3 and img_array.shape[2] == 3:  # RGB image
            pass  # No conversion needed
        else:
            raise ValueError("Unexpected image dimensions or channels")
        
        return img_array.resize(1, 150, 150, 3)

def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        base64_string = base64.b64encode(file.read()).decode('utf-8')
    return base64_string

def load_label_encoder(encoder_path):
    with open(encoder_path, "rb") as f:
        label_encoder = pickle.load(f)
    return label_encoder
