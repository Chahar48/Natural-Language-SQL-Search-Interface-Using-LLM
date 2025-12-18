import streamlit as st
from typing import List, Dict, Any

from app.llm.sql_generator import generate_sql_from_nl
from app.search.hybrid_search import hybrid_search
from app.validators.sql_validator import validate_sql_query


# Streamlit Page Config -----------------------------------------------
st.set_page_config(
    page_title="Natural Language SQL Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Natural Language SQL Search Interface")
st.markdown(
    """
    Ask questions in **plain English** and get results directly from the database.
    
    **Examples:**
    - *List all employees in the Engineering department*
    - *Show expensive products*
    - *Orders handled in December 2024*
    """
)


# User Input ----------------------------------------------------------
user_query = st.text_input(
    "Enter your question:",
    placeholder="e.g. List all employees in the Engineering department"
)

search_clicked = st.button("Search")


# Search Execution  ---------------------------------------------------
if search_clicked:
    if not user_query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Processing your query..."):
            try:
                # Step 1: NL → SQL
                generated_sql = generate_sql_from_nl(user_query)

                if not generated_sql:
                    st.error("Failed to generate SQL from the query.")
                    st.stop()

                # Show generated SQL (transparent & recruiter-friendly)
                with st.expander("Generated SQL"):
                    st.code(generated_sql, language="sql")

                # Step 2: Validate SQL
                if not validate_sql_query(generated_sql):
                    st.error("Generated SQL failed safety validation.")
                    st.stop()

                # Step 3: Hybrid Search Execution
                results: List[Dict[str, Any]] = hybrid_search(
                    user_query=user_query,
                    generated_sql=generated_sql
                )

                # Step 4: Display Results
                if results:
                    st.success(f"Found {len(results)} result(s)")
                    st.dataframe(results, use_container_width=True)
                else:
                    st.info("No results found.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
