-- =========================================================
-- Enable pgvector extension (required for vector embeddings)
-- =========================================================

CREATE EXTENSION IF NOT EXISTS vector;



-- Departments Table

CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);



-- Employees Table

CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    salary DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES departments(id)
        ON DELETE RESTRICT
);



-- Orders Table

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    employee_id INT NOT NULL,
    order_total DECIMAL(10,2) NOT NULL,
    order_date DATE NOT NULL,

    -- Vector embedding for semantic search on customer name
    customer_name_embedding VECTOR(384),

    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(id)
        ON DELETE RESTRICT
);



-- Products Table

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    -- Vector embedding for semantic search on product name
    name_embedding VECTOR(384)
);