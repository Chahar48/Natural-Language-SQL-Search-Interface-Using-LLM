
# from app.utils.config import DB_NAME, GROQ_MODEL

# print(DB_NAME)
# print(GROQ_MODEL)


# test_db_connection.py ...............................................

# from app.db.connection import engine

# try:
#     with engine.connect() as connection:
#         print("✅ Database connection successful")
# except Exception as e:
#     print("❌ Database connection failed:", e)


#test_embeddings.py   ...............................................
# from app.embeddings.embedder import generate_embedding

# text = "Laptop Pro 15"
# embedding = generate_embedding(text)

# print("Embedding length:", len(embedding))
# print("First 5 values:", embedding[:5])


#test_sql_generator.py  ...............................................
# from app.llm.sql_generator import generate_sql_from_nl

# query = "List all employees in the Engineering department"
# sql = generate_sql_from_nl(query)

# print("Generated SQL:")
# print(sql)


#test_sql_validator.py   ...............................................
# from app.validators.sql_validator import validate_sql_query

# safe_sql = """
# SELECT e.name, e.salary
# FROM employees e
# JOIN departments d ON e.department_id = d.id
# WHERE d.name = 'Engineering';
# """

# dangerous_sql = "DROP TABLE employees;"

# print("Safe SQL:", validate_sql_query(safe_sql))
# print("Dangerous SQL:", validate_sql_query(dangerous_sql))


#test_sql_executor.py   ...............................................
# from app.search.sql_executor import execute_sql_query

# sql = """
# SELECT e.name, e.salary
# FROM employees e
# JOIN departments d ON e.department_id = d.id
# WHERE d.name = 'Engineering';
# """

# results = execute_sql_query(sql)

# print(results)



#test_hybrid_search.py ----------------------------------------------
# from app.llm.sql_generator import generate_sql_from_nl
# from app.search.hybrid_search import hybrid_search

# query = "List all employees in the Engineering department"
# sql = generate_sql_from_nl(query)

# results = hybrid_search(query, sql)
# print(results)