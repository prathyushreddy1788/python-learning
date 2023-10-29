CREATE TABLE Sales (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Date DATE
);

INSERT INTO Sales (OrderID, ProductID, Quantity, Date) VALUES
(1, 101, 5, '2023-10-01'),
(2, 102, 3, '2023-10-02'),
(3, 101, 2, '2023-10-02'),
(4, 103, 7, '2023-10-03'),
(5, 102, 4, '2023-10-03');
