import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd

def transform_image(image, target_size=(150, 150)):
    """Las imágenes original se transforman para que cada una de estas tenga el mismo número de canales y dimensiones. La imagen en img_path se convierte en una de formato RGB

    Args:
        img: la imagen abierta a transformar
        target_size (tuple, optional): Dimensiones objetivo con las que se estandarizan todas las imágenes. Defaults to (150, 150).

    Returns:
        array: imagen convertida a array y en RGB
    """
    if type(image) is str:
        with Image.open(image) as image:
            img = image.resize(target_size)
            img_array = np.asarray(img)
            if img_array.ndim == 2:  # Grayscale image
                # Convert grayscale to RGB by stacking the same channel three times
                img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
            elif img_array.ndim == 3 and img_array.shape[2] == 4:  # RGBA image
                # Convert RGBA to RGB by removing the alpha channel
                img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
            elif img_array.ndim == 3 and img_array.shape[2] == 3:  # RGB image
                pass  # No conversion needed
            return img_array
    else:
        img = image.resize(target_size)
        img_array = np.asarray(img)
        if img_array.ndim == 2:  # Grayscale image
            # Convert grayscale to RGB by stacking the same channel three times
            img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
        elif img_array.ndim == 3 and img_array.shape[2] == 4:  # RGBA image
            # Convert RGBA to RGB by removing the alpha channel
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
        elif img_array.ndim == 3 and img_array.shape[2] == 3:  # RGB image
            pass  # No conversion needed
        return img_array

def retrieve_images(path):
    corrupted_images = 0
    images_path = []
    images_type = []
    images_array = []
    duplicated_images = 0
    images_set = set() 

    classes = os.listdir(path) 

    for class_ in classes:
        base_path = os.path.join(path, class_)
        for file in os.listdir(base_path):
            file_path = os.path.join(base_path, file)
            try:
                with Image.open(file_path) as image:
                    image_matrix = transform_image(image)
                    image_tuple = tuple(image_matrix.flatten())

                    if image_tuple in images_set:
                        duplicated_images += 1
                    else:
                        images_type.append(class_)
                        images_path.append(file_path)
                        images_array.append(image_matrix)
                        images_set.add(image_tuple)

            except Image.UnidentifiedImageError:
                corrupted_images += 1

    print(f'Se procesaron {len(images_array)} imágenes correctamente.')
    print(f'{corrupted_images} no pudieron ser procesadas por errores en formato.')
    print(f'Se encontraron {duplicated_images} imágenes duplicadas')
    images_df = pd.DataFrame({'matriz': images_array, 'clase': images_type, 'ruta': images_path})
    return images_df