-- Create the Customers table
CREATE TABLE Customers (
    CustomerID INT,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    PRIMARY KEY (CustomerID)
);
 
-- Insert sample data into the Customers table
INSERT INTO Customers (CustomerID, CustomerName, City)
VALUES
    (1, 'John', 'New York'),
    (2, 'Jane', 'London'),
    (3, 'Mike', 'Paris');

-- Create the Products table
CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(100),
    Price DECIMAL(10, 2),
    PRIMARY KEY (ProductID)
);

-- Insert sample data into the Products table
INSERT INTO Products (ProductID, ProductName, Category, Price)
VALUES
    (1, 'Product A', 'Category 1', 10.99),
    (2, 'Product B', 'Category 2', 25.49),
    (3, 'Product C', 'Category 1', 15.99);

-- Create the Orders table
CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    OrderDate DATE,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert sample data into the Orders table
INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES
    (1, 1, '2021-01-10'),
    (2, 2, '2021-02-15'),
    (3, 1, '2021-03-20');

-- Create the OrderDetails table
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert sample data into the OrderDetails table
INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES
    (1, 1, 2),
    (1, 2, 1),
    (2, 3, 3),
    (3, 1, 2),
    (3, 2, 2),
    (3, 3, 1);

