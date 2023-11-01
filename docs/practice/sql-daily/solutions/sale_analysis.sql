SELECT
    productid,
    SUM(quantity) AS total_quantity
FROM Sales
GROUP BY productid;


SELECT
        ProductID,
        sum(Quantity)
FROM sales where Date = "2023-10-02"
group by ProductID;