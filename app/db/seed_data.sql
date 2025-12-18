-- =========================================================
-- Seed Data for Departments
-- =========================================================
INSERT INTO departments (name) VALUES
('HR'),
('Engineering'),
('Sales'),
('Marketing'),
('Finance');


-- =========================================================
-- Seed Data for Employees
-- =========================================================

INSERT INTO employees (name, department_id, email, salary) VALUES
('Amit Sharma', 2, 'amit.sharma@company.com', 85000.00),
('Neha Verma', 1, 'neha.verma@company.com', 60000.00),
('Rohit Singh', 3, 'rohit.singh@company.com', 70000.00),
('Priya Mehta', 2, 'priya.mehta@company.com', 95000.00),
('Karan Malhotra', 4, 'karan.malhotra@company.com', 65000.00),
('Sneha Iyer', 5, 'sneha.iyer@company.com', 90000.00);


-- =========================================================
-- Seed Data for Products
-- =========================================================
INSERT INTO products (name, price) VALUES
('Laptop Pro 15', 120000.00),
('Wireless Mouse', 1500.00),
('Mechanical Keyboard', 4500.00),
('Noise Cancelling Headphones', 18000.00),
('27-inch Monitor', 22000.00),
('USB-C Docking Station', 9000.00);


-- =========================================================
-- Seed Data for Orders
-- =========================================================

INSERT INTO orders (customer_name, employee_id, order_total, order_date) VALUES
('Rajesh Kumar', 1, 125000.00, '2024-11-05'),
('Anita Desai', 3, 18000.00, '2024-11-10'),
('Vikas Gupta', 2, 4500.00, '2024-11-12'),
('Pooja Nair', 4, 22000.00, '2024-12-01'),
('Suresh Reddy', 1, 9000.00, '2024-12-03'),
('Meenal Joshi', 5, 1500.00, '2024-12-05'),
('Arjun Patel', 3, 120000.00, '2024-12-08'),
('Kavita Rao', 6, 18000.00, '2024-12-10');
