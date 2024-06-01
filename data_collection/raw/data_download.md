# Data Collection

## Context
Dataset for classifying different styles of art. Main categories have been taken here

## Content
5 kinds of data downloaded from google images, yandex images and this site:
- Drawings and watercolours
- Works of painting
- Sculpture
- Graphic Art
- Iconography (old Russian art)

Data is separated on training and validation sets

## Data Location
The data for this project can be found in [this Kaggle project](https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving).

Two approaches can be used to download the data:

### 1. Use Web Interface
1. Log in to your Kaggle account.
2. Navigate to the dataset page.
3. Click the "Download" button to download the dataset.

### 2. Using Kaggle CLI
1. Install Kaggle API:

    ```sh
    pip install kaggle
    ```

2. Use the following command to download the zip files:

    ```sh
    kaggle datasets download -d thedownhill/art-images-drawings-painting-sculpture-engraving
    ```

3. Extract the data from the zip file.