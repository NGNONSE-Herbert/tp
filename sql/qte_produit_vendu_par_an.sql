USE classicmodels;
select  year(shippedDate), count(quantityOrdered) as quantite
from orders
INNER JOIN orderdetails on orderdetails.orderNumber = orders.orderNumber
where status = "Shipped"
group by year(shippedDate) 
order by year(shippedDate);