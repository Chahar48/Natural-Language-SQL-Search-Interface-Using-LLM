from groq import Groq
from typing import Optional

from app.llm.prompt import SQL_GENERATION_PROMPT
from app.utils.config import GROQ_API_KEY, GROQ_MODEL



# Initialize Groq client (once)
groq_client = Groq(api_key=GROQ_API_KEY)



# Generate SQL from Natural Language
def generate_sql_from_nl(user_query: str) -> Optional[str]:
    """
    Converts a natural language query into a SQL query using Groq LLM.

    Args:
        user_query (str): User's natural language question

    Returns:
        Optional[str]: Generated SQL query as a string, or None on failure
    """
    if not user_query or not user_query.strip():
        raise ValueError("User query cannot be empty")

    # Format prompt with user query
    prompt = SQL_GENERATION_PROMPT.format(user_query=user_query)

    try:
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.0,  # Low temperature = deterministic SQL
            max_tokens=512
        )

        # Extract raw SQL text
        sql_query = response.choices[0].message.content.strip()

        return sql_query

    except Exception as e:
        # In production, log this instead of printing
        print(f"Error generating SQL from LLM: {e}")
        return None
