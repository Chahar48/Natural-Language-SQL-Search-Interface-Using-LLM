# Natural-Language-SQL-Search-Interface-Using-LLM
A secure and intelligent Natural Language → SQL search system built using Groq LLM, PostgreSQL + pgvector, SQLAlchemy, and Streamlit. The system allows users to query a relational database in plain English, with strong safety guarantees and hybrid semantic search. 


## 🚀 Project Overview

This project demonstrates how modern LLMs can be safely integrated with traditional databases to enable:

 - Natural language querying of structured data
 - Secure SQL generation and execution
 - Hybrid retrieval using structured SQL + vector similarity
 - Clean, modular, production-style architecture
 - The solution is designed, emphasizing:
 - Security
 - Separation of concerns
 - Explainability
 - Real-world design decisions


## 🧱 System Architecture
User (Streamlit UI)
        ↓
Natural Language Query
        ↓
Groq LLM (NL → SQL)
        ↓
SQL Validator (Security Gate)
        ↓
Hybrid Search Logic
   ├── Pure SQL Execution
   └── pgvector Semantic Search
        ↓
PostgreSQL (Dockerized)
        ↓
Results → Streamlit UI


## 🗂️ Project Structure
AI_SQL_Search_Interface/
│
├── app/
│   ├── main.py                 # Streamlit UI (thin layer)
│
│   ├── db/
│   │   ├── connection.py       # SQLAlchemy DB connection
│   │   ├── schema.sql          # Database schema
│   │   └── seed_data.sql       # Sample data
│
│   ├── embeddings/
│   │   └── embedder.py         # Text → vector embeddings
│
│   ├── llm/
│   │   ├── prompt.py           # Strict NL → SQL prompt
│   │   └── sql_generator.py    # Groq LLM integration
│
│   ├── search/
│   │   ├── sql_executor.py     # Safe SQL execution
│   │   └── hybrid_search.py    # SQL + vector search
│
│   ├── validators/
│   │   └── sql_validator.py    # SQL injection prevention
│
├── requirements.txt
├── .env
└── README.md



🛠️ Tech Stack

LLM: Groq (NL → SQL generation)
Database: PostgreSQL + pgvector (Dockerized)
Embeddings: SentenceTransformers (384-dim vectors)
ORM / DB Access: SQLAlchemy
UI: Streamlit
Language: Python 3.10+


⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your-github-repo-url>
cd AI_SQL_Search_Interface

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start PostgreSQL + pgvector (Docker)
docker run -d \
  --name pgvector-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=query_search_db \
  -p 5432:5432 \
  pgvector/pgvector:pg15

5️⃣ Create Tables & Seed Data

Use pgAdmin → Query Tool to run:

app/db/schema.sql

app/db/seed_data.sql

6️⃣ Configure Environment Variables

Create .env file:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=query_search_db
DB_USER=postgres
DB_PASSWORD=postgres

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

7️⃣ Run the Application
python -m streamlit run app/main.py


Open browser:

http://localhost:8501

🧪 Sample Queries
Structured Queries
List all employees in the Engineering department
Show all orders handled in December 2024
Who is the highest paid employee?

Semantic / Hybrid Queries
Show expensive products
List cheap products
Find customers similar to Rajesh Kumar

Security Test (Blocked)
Drop the employees table


🔐 Security & Safety Design

LLM output is never executed directly

Strict SQL validation enforces:

 - SELECT-only queries
 - Schema whitelisting
 - Alias resolution
 - Injection prevention
 - Execution happens only after validation
 - This ensures production-grade safety.


🧠 Key Design Decisions
Q)Why Groq for NL → SQL?
Extremely fast inference

Q)Deterministic outputs with low temperature
Ideal for real-time NL → SQL conversion

Q)Why SentenceTransformers for embeddings?
Groq does not provide embeddings

Q)SentenceTransformers integrate cleanly with pgvector
Common real-world architecture pattern

Q)Why Hybrid Search?
Not all queries need embeddings

Q)Structured SQL is more reliable for filters
Semantic search improves relevance for fuzzy queries

📈 Future Improvements

* Result ranking & scoring
* Query caching (Redis)
* Authentication & role-based access
* Streaming LLM responses
* Multi-database support
* Agent-based query planning


🎯 Evaluation Alignment

This project demonstrates:

✔ Secure AI usage
✔ Clean modular architecture
✔ SQL & DB fundamentals
✔ LLM control & prompt engineering
✔ Production-ready thinking


👤 Author
Mukesh Kumar
