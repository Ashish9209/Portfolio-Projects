-- DATABASE DESIGN

-- Categories
-- ------------
-- category_id (PK)
-- category_name

-- Suppliers
-- ------------
-- supplier_id (PK)
-- supplier_name
-- contact_info

-- Products
-- ------------
-- product_id (PK)
-- product_name
-- category_id (FK)
-- supplier_id (FK)
-- price
-- stock_quantity

-- Inventory
-- ------------
-- transaction_id (PK)
-- product_id (FK)
-- transaction_date
-- quantity
-- transaction_type (IN/OUT)



-- DATABASE SETUP

-- Create the database
CREATE DATABASE inventory_management;

-- Connect to the database
\c inventory_management

-- Create tables

-- Categories table
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Suppliers table
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_info TEXT
);

-- Products table
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT REFERENCES Categories(category_id),
    supplier_id INT REFERENCES Suppliers(supplier_id),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

-- Inventory table
CREATE TABLE Inventory (
    transaction_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES Products(product_id),
    transaction_date DATE NOT NULL,
    quantity INT NOT NULL,
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('IN', 'OUT'))
);


-- Insert categories
INSERT INTO Categories (category_name) VALUES
('Electronics'),
('Furniture'),
('Clothing');

-- Insert suppliers
INSERT INTO Suppliers (supplier_name, contact_info) VALUES
('Supplier A', '123-456-7890'),
('Supplier B', '098-765-4321');

-- Insert products
INSERT INTO Products (product_name, category_id, supplier_id, price, stock_quantity) VALUES
('Laptop', 1, 1, 999.99, 50),
('Desk Chair', 2, 2, 149.99, 30),
('T-Shirt', 3, 1, 19.99, 100);

-- Insert inventory transactions
INSERT INTO Inventory (product_id, transaction_date, quantity, transaction_type) VALUES
(1, '2024-08-01', 10, 'IN'),
(1, '2024-08-03', 5, 'OUT'),
(2, '2024-08-02', 15, 'IN'),
(3, '2024-08-05', 25, 'OUT');



--  ADVANCED QUERIES

-- Query: Get Current Stock Levels

SELECT p.product_name, p.stock_quantity
FROM Products p;

-- Query: Total Stock Value by Category

SELECT c.category_name, SUM(p.stock_quantity * p.price) AS total_stock_value
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name;

-- Query: Recent Inventory Transactions for a Product

SELECT p.product_name, i.transaction_date, i.quantity, i.transaction_type
FROM Inventory i
JOIN Products p ON i.product_id = p.product_id
WHERE p.product_name = 'Laptop'
ORDER BY i.transaction_date DESC;

-- Query: Low Stock Alert

SELECT product_name, stock_quantity
FROM Products
WHERE stock_quantity < 20;

-- Query: Product Stock History

SELECT p.product_name, i.transaction_date, i.quantity, i.transaction_type
FROM Inventory i
JOIN Products p ON i.product_id = p.product_id
WHERE i.transaction_date BETWEEN '2024-08-01' AND '2024-08-31'
ORDER BY i.transaction_date;



