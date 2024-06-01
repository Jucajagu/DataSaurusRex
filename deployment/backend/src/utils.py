from PIL import Image
import base64
import numpy as np
import pickle

def read_image_as_numpy_array(image_file, target_size=(150, 150)):
    img = Image.open(image_file)
    img = img.convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        base64_string = base64.b64encode(file.read()).decode('utf-8')
    return base64_string

def load_label_encoder(encoder_path):
    with open(encoder_path, "rb") as f:
        label_encoder = pickle.load(f)
    return label_encoder
