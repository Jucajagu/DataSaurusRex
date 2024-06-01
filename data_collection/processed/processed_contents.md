# Directory Contents

This directory contains four files essential for the image classification project. Below is a detailed description of each file:

1. **embedding_images.csv**
    - **Description**: This CSV file contains the embeddings produced by the output of a neural network model.
    - **Details**:
        - The embeddings consist of 128 fields, representing the images' similarity in a hyperspace.
        - It includes a column for the file location name in the data lake bucket.
        - It also contains a column for the label indicating the type of image (e.g., painting, sculpture).

2. **sample_X.npy**
    - **Description**: This NumPy file contains a sample of 100 images in matrix form.
    - **Details**:
        - The images are of size 150x150 pixels.
        - These images were used in model training.

3. **sample_y_encoded.npy**
    - **Description**: This NumPy file contains the labels for a sample of 100 images.
    - **Details**:
        - The labels are in text form.

4. **sample_y.npy**
    - **Description**: This NumPy file contains the labels for a sample of 100 images.
    - **Details**:
        - The labels are in numerical form, ready for one-hot encoding (dummyfying).

## File Summaries

### embedding_images.csv

| location              | label      | 0 | 1 | ... | 127 |
|----------------------------|------------|-------------|-------------|-----|---------------|
| /path/image1.jpg | painting   | 0.123       | 0.456       | ... | 0.789         |
| /path/image2.jpg | sculpture  | 0.234       | 0.567       | ... | 0.890         |

### sample_y_encoded.npy

- **Shape**: `(100,)`
- Contains text labels for the 100 images, e.g., `["painting", "sculpture", ...]`.

### sample_y.npy

- **Shape**: `(100,)`
- Contains numerical labels for the 100 images, e.g., `[0, 1, ...]`.