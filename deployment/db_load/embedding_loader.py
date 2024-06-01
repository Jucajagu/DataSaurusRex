import pandas as pd
import psycopg2
from psycopg2.extensions import register_adapter, AsIs
import numpy as np
from tqdm import tqdm

# Register numpy array adapter to be used with psycopg2
def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))

register_adapter(np.ndarray, addapt_numpy_array)

# Load the CSV file
df = pd.read_csv('embedding_images.csv')

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="bigdata*",
    host="analitica.cakbsuyk0vne.us-east-1.rds.amazonaws.com",
    port="5432"
)
cur = conn.cursor()

total_rows = len(df)

# Insert data into the table
with tqdm(total=total_rows, desc="Inserting data") as pbar:
    for index, row in df.iterrows():
        # Convert embedding data to a list of floats
        embedding_data = [float(val) for val in row[df.columns.drop(["location", "label"])]]
        cur.execute(
            "INSERT INTO image_embeddings (location, label, embedding) VALUES (%s, %s, %s)",
            (row['location'], row['label'], embedding_data)
        )
        pbar.update(1)

# Commit and close the connection
conn.commit()
cur.close()
conn.close()