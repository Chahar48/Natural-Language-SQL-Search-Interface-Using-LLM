import re
from typing import Dict


# Allowed tables and columns 
ALLOWED_TABLES = {
    "departments": {"id", "name"},
    "employees": {"id", "name", "department_id", "email", "salary"},
    "orders": {"id", "customer_name", "employee_id", "order_total", "order_date"},
    "products": {"id", "name", "price"},
}


# Disallowed SQL keywords (SECURITY)
FORBIDDEN_KEYWORDS = {
    "insert", "update", "delete", "drop", "alter", "truncate",
    "create", "grant", "revoke", "commit", "rollback",
    "execute", "call"
}


# Main SQL validation function
def validate_sql_query(sql: str) -> bool:
    if not sql or not sql.strip():
        return False

    normalized_sql = sql.strip().lower()

    # Rule 1: Must start with SELECT
    if not normalized_sql.startswith("select"):
        return False

    # Rule 2: Block multiple statements
    if ";" in normalized_sql[:-1]:
        return False

    # Rule 3: Block forbidden keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", normalized_sql):
            return False

    # Rule 4: Validate schema usage
    return _validate_tables_and_columns(normalized_sql)


# Helper: Validate tables, aliases, and columns

def _validate_tables_and_columns(sql: str) -> bool:
    """
    Validates that:
    - Only allowed tables are used
    - Aliases map to valid tables
    - Columns belong to correct tables
    """

    
    # Step 1: Extract table → alias mappings
    # e.g. "employees e", "departments d"
    table_aliases: Dict[str, str] = {}

    table_matches = re.findall(
        r"(from|join)\s+([a-z_]+)(?:\s+([a-z_]+))?",
        sql
    )

    for _, table, alias in table_matches:
        if table not in ALLOWED_TABLES:
            return False
        table_aliases[alias or table] = table

    
    # Step 2: Validate column references
    # e.g. e.name → employees.name
    column_matches = re.findall(r"([a-z_]+)\.([a-z_]+)", sql)

    for alias, column in column_matches:
        if alias not in table_aliases:
            return False

        real_table = table_aliases[alias]
        if column not in ALLOWED_TABLES[real_table]:
            return False

    return True
