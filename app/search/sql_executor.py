from typing import List, Dict, Any
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.connection import engine


# Execute validated SQL query safely
def execute_sql_query(sql: str) -> List[Dict[str, Any]]:
    """
    Executes a validated SQL SELECT query and returns results.

    Args:
        sql (str): Validated SQL query (SELECT only)

    Returns:
        List[Dict[str, Any]]: Query result as list of dictionaries
    """
    if not sql or not sql.strip():
        raise ValueError("SQL query is empty")

    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql))

            # Convert result rows to list of dicts
            rows = result.fetchall()
            columns = result.keys()

            return [dict(zip(columns, row)) for row in rows]

    except SQLAlchemyError as e:
        # In production, use structured logging
        raise RuntimeError(f"Database execution error: {e}")
