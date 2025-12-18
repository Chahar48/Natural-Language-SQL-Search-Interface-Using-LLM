from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

from app.utils.config import EMBEDDING_MODEL


# Load embedding model ONCE (important for performance)
_embedding_model = SentenceTransformer(EMBEDDING_MODEL)



# Generate embedding for a single text
def generate_embedding(text: str) -> List[float]:
    """
    Convert a single text string into a vector embedding.

    Args:
        text (str): Input text (e.g., product name, customer name)

    Returns:
        List[float]: Vector embedding compatible with pgvector
    """
    if not text or not text.strip():
        raise ValueError("Input text for embedding is empty")

    embedding = _embedding_model.encode(text)

    # Convert numpy array to Python list for pgvector compatibility
    return embedding.tolist()



# Generate embeddings for multiple texts (batch)
def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Convert multiple text strings into vector embeddings.

    Args:
        texts (List[str]): List of input texts

    Returns:
        List[List[float]]: List of vector embeddings
    """
    if not texts:
        raise ValueError("Input text list is empty")

    embeddings = _embedding_model.encode(texts)

    return [emb.tolist() for emb in embeddings]
