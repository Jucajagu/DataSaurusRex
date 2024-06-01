from db_router import SessionLocal, ImageEmbedding, select


def find_nearest_neighbors(embedding, label):
    session = SessionLocal()
    list_embedding = embedding.tolist()[0]

    # Perform the query
    query_result = session.execute(
        select(ImageEmbedding)
        .filter(ImageEmbedding.label == label)
        .order_by(ImageEmbedding.embedding.cosine_distance(list_embedding))
        .limit(5)
    )

    # Extract locations from the query result
    neighbors = [
        {"location": row[0].location, "label": row[0].label} for row in query_result
    ]

    session.close()
    return neighbors
