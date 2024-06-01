from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pgvector.sqlalchemy import Vector

# Define SQLAlchemy models
Base = declarative_base()


class ImageEmbedding(Base):
    __tablename__ = "image_embeddings"

    id = Column(Integer, primary_key=True)
    label = Column(String)
    location = Column(String)
    embedding = Column(Vector(128))


# Create database connection
engine = create_engine(
    "postgresql://postgres:bigdata*@analitica.cakbsuyk0vne.us-east-1.rds.amazonaws.com/postgres"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
