from typing import List, Dict, Any
from sqlalchemy import text

from app.db.connection import engine
from app.embeddings.embedder import generate_embedding
from app.search.sql_executor import execute_sql_query
from app.validators.sql_validator import validate_sql_query


# Heuristic: Decide if semantic search is needed
def _requires_semantic_search(user_query: str) -> bool:
    """
    Simple heuristic to decide whether to use vector search.
    """
    semantic_keywords = [
        "similar",
        "related",
        "like",
        "expensive",
        "cheap",
        "high value",
        "low cost",
        "top",
        "best"
    ]

    query_lower = user_query.lower()
    return any(keyword in query_lower for keyword in semantic_keywords)



# Vector similarity search (pgvector)
def _vector_search(
    table: str,
    embedding_column: str,
    query_embedding: List[float],
    limit: int = 5
) -> List[Dict[str, Any]]:
    """
    Performs vector similarity search using pgvector.
    """
    sql = f"""
    SELECT *,
           {embedding_column} <-> :embedding AS distance
    FROM {table}
    ORDER BY distance
    LIMIT :limit;
    """

    with engine.connect() as connection:
        result = connection.execute(
            text(sql),
            {
                "embedding": query_embedding,
                "limit": limit
            }
        )

        rows = result.fetchall()
        columns = result.keys()

        return [dict(zip(columns, row)) for row in rows]



# Hybrid Search (MAIN ENTRY POINT)
def hybrid_search(
    user_query: str,
    generated_sql: str
) -> List[Dict[str, Any]]:
    """
    Executes either pure SQL or hybrid (SQL + vector) search
    based on query intent.
    """

    # Step 1: Always validate SQL first
    if not validate_sql_query(generated_sql):
        raise ValueError("Generated SQL failed validation")

    # Step 2: Decide search strategy
    use_semantic = _requires_semantic_search(user_query)

    
    # Step 3: Semantic search paths
    if use_semantic:
        query_embedding = generate_embedding(user_query)

        # Product semantic search
        if "product" in user_query.lower():
            return _vector_search(
                table="products",
                embedding_column="name_embedding",
                query_embedding=query_embedding
            )

        # Customer semantic search
        if "customer" in user_query.lower() or "order" in user_query.lower():
            return _vector_search(
                table="orders",
                embedding_column="customer_name_embedding",
                query_embedding=query_embedding
            )

    # Step 4: Default → pure SQL execution
    return execute_sql_query(generated_sql)
