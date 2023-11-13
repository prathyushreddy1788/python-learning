SELECT customername,count(*)
from Customers inner join Orders
on Customers.CustomerID = Orders.CustomerID
inner join orderdetails on orders.OrderID = orderdetails.OrderID
group by customername
HAVING count(*) >= 3


select Category,avg(Price*Quantity) as avg_price from
products inner join orderdetails
on products.ProductID = orderdetails.ProductID
group by Category


SELECT customername,sum(quantity*price)
from Customers inner join orders
on Customers.CustomerID = Orders.CustomerID
inner join orderdetails on orders.OrderID = orderdetails.OrderID
inner join products on orderdetails.ProductID = products.ProductID
group by customername


select CustomerName,count(*) as no_of_orders
from customers inner join orders
on customers.CustomerID = orders.CustomerID
where YEAR(orderdate) = 2021
group by CustomerName


use mydb;
select customername,count(orders.orderID) as no_of_orders  from
customers left join orders
on customers.CustomerID = orders.CustomerID
left join orderdetails
on orders.OrderID = orderdetails.OrderID
group by CustomerName,orders.OrderID
order by no_of_orders desc


use mydb;
select ProductName,sum(quantity) as total_quantity,avg(Quantity*price) as avg_price_per_unit from
products inner join orderdetails
on products.ProductID = orderdetails.ProductID
group by ProductName

use mydb;
select customername,sum(price*quantity) as expenses from
customers left join orders on
customers.customerid = orders.customerid
left join orderdetails on
orders.orderid = orderdetails.orderid
left join products on
orderdetails.productid = products.productid
group by customername
order by expenses desc


use mydb;
select customername,orderdate,price*Quantity as expenses from
customers left join orders on
customers.CustomerID = orders.CustomerID
left join orderdetails on
orders.orderid = orderdetails.orderid
left join products on
orderdetails.productid = products.ProductID





