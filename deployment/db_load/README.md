# Script Description

This script is designed to load the `embedding_images.csv` file located [here](../../data_collection/processed/). The script performs the following tasks:

1. **Loads the CSV File**: It reads the `embedding_images.csv` file, which contains the embeddings of images produced by a neural network model. The CSV includes columns for the image's file location in the data lake, the image label, and the 128-dimensional embedding.

2. **Connects to AWS RDS**: It establishes a connection to an AWS RDS (Relational Database Service) instance using the `psycopg2` library for PostgreSQL.

3. **Inserts Data into the Database**: It iterates through each record in the CSV file and inserts the image's file location, label, and embedding into the AWS RDS database.

For more details on the structure and contents of the `embedding_images.csv` file, refer to the [processed_contents](../../data_collection/processed/processed_contents.md) documentation.
