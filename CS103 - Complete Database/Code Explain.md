Break down the SQL code, which includes schema design, table creation, data insertion, and queries for an inventory management database using PostgreSQL.

### Schema Design

The schema design section outlines the structure of the database and the relationships between tables.

1. **Categories Table**
   - **`category_id`**: Primary Key (PK), uniquely identifies each category.
   - **`category_name`**: Name of the category (e.g., Electronics, Furniture).

2. **Suppliers Table**
   - **`supplier_id`**: Primary Key (PK), uniquely identifies each supplier.
   - **`supplier_name`**: Name of the supplier.
   - **`contact_info`**: Additional contact information for the supplier.

3. **Products Table**
   - **`product_id`**: Primary Key (PK), uniquely identifies each product.
   - **`product_name`**: Name of the product.
   - **`category_id`**: Foreign Key (FK) referencing `Categories(category_id)`, categorizes the product.
   - **`supplier_id`**: Foreign Key (FK) referencing `Suppliers(supplier_id)`, identifies the supplier of the product.
   - **`price`**: Price of the product.
   - **`stock_quantity`**: Quantity of the product in stock.

4. **Inventory Table**
   - **`transaction_id`**: Primary Key (PK), uniquely identifies each inventory transaction.
   - **`product_id`**: Foreign Key (FK) referencing `Products(product_id)`, identifies the product involved in the transaction.
   - **`transaction_date`**: Date of the transaction.
   - **`quantity`**: Quantity of the product involved in the transaction.
   - **`transaction_type`**: Type of transaction (`IN` for restocking, `OUT` for sales or deductions). 

### SQL Commands

#### Create the Database and Connect

```sql
-- Create the database
CREATE DATABASE inventory_management;

-- Connect to the database
\c inventory_management
```
- **`CREATE DATABASE inventory_management;`**: Creates a new database named `inventory_management`.
- **`\c inventory_management`**: Connects to the `inventory_management` database.

#### Create Tables

```sql
-- Create Categories table
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Create Suppliers table
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_info TEXT
);

-- Create Products table
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT REFERENCES Categories(category_id),
    supplier_id INT REFERENCES Suppliers(supplier_id),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

-- Create Inventory table
CREATE TABLE Inventory (
    transaction_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES Products(product_id),
    transaction_date DATE NOT NULL,
    quantity INT NOT NULL,
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('IN', 'OUT'))
);
```

- **`SERIAL`**: Automatically increments integer values for primary keys.
- **`VARCHAR(n)`**: Variable character field with a maximum length of `n`.
- **`INT`**: Integer type.
- **`DECIMAL(10, 2)`**: Numeric type with 10 digits in total and 2 digits after the decimal point.
- **`CHECK`**: Enforces a constraint to ensure `transaction_type` is either 'IN' or 'OUT'.

#### Insert Sample Data

```sql
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
```
- **`INSERT INTO`**: Adds new records to the specified table.

#### Query Examples

1. **Get Current Stock Levels**

   ```sql
   SELECT p.product_name, p.stock_quantity
   FROM Products p;
   ```
   - **Purpose**: Retrieves the current stock levels of all products.

2. **Total Stock Value by Category**

   ```sql
   SELECT c.category_name, SUM(p.stock_quantity * p.price) AS total_stock_value
   FROM Products p
   JOIN Categories c ON p.category_id = c.category_id
   GROUP BY c.category_name;
   ```
   - **Purpose**: Calculates the total stock value for each category by multiplying stock quantity with product price and summing up.

3. **Recent Inventory Transactions for a Product**

   ```sql
   SELECT p.product_name, i.transaction_date, i.quantity, i.transaction_type
   FROM Inventory i
   JOIN Products p ON i.product_id = p.product_id
   WHERE p.product_name = 'Laptop'
   ORDER BY i.transaction_date DESC;
   ```
   - **Purpose**: Retrieves recent inventory transactions for the 'Laptop' product, ordered by date in descending order.

4. **Low Stock Alert**

   ```sql
   SELECT product_name, stock_quantity
   FROM Products
   WHERE stock_quantity < 20;
   ```
   - **Purpose**: Identifies products with stock quantities below 20.

5. **Product Stock History**

   ```sql
   SELECT p.product_name, i.transaction_date, i.quantity, i.transaction_type
   FROM Inventory i
   JOIN Products p ON i.product_id = p.product_id
   WHERE i.transaction_date BETWEEN '2024-08-01' AND '2024-08-31'
   ORDER BY i.transaction_date;
   ```
   - **Purpose**: Retrieves the history of inventory transactions for all products within the specified date range.




